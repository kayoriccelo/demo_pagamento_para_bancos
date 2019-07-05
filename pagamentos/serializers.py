import datetime
from collections import OrderedDict

from pkg_resources._vendor.pyparsing import empty
from rest_framework import serializers

from contratos.models import Conta, Empresa
from febraban import builders
from febraban.processos import ProcessoPagamentoFebraban


class PagamentoOnlineSerializer(serializers.Serializer):

    def __init__(self, instance=None, data=empty, **kwargs):
        super(PagamentoOnlineSerializer, self).__init__(instance, data, **kwargs)

        # TODO - Kayo Riccelo: estes dados vem do frontend conforme as configurações do usuario
        conta = Conta()
        self.params = {
            'conta': conta,
            'data_pagamento': '01/07/2016',
            'dia_vencimento': '05',
        }

        for key in [field for field in conta.leiaute_fbb_brad.__dir__() if field.find('__') == -1]:
            self.params[key] = conta.leiaute_fbb_brad.__getattribute__(key)

    def _get_processo_pagamento(self):
        if self.validated_data['tipo_pagamento'] == 'febraban':
            self.processo = ProcessoPagamentoFebraban

    def _get_builder(self):
        if self.validated_data['conta'].codigo_banco == '107':
            self.builder = builders.PagamentoOnlineFBBBradescoBuilder
        elif self.validated_data['conta'].codigo_banco == '104':
            self.builder = builders.PagamentoOnlineFBBCEFBuilder
        elif self.validated_data['conta'].codigo_banco == '001':
            self.builder = builders.PagamentoOnlineFBBBancoBrasilBuilder

        self._get_processo_pagamento()

    def validate(self, attrs):
        attrs['contratos'] = self.context['contratos']

        if 'conta' in self.params:
            attrs['conta'] = self.params.pop('conta')
        else:
            raise serializers.ValidationError({'error': 'Conta não encontrada.'})

        if 'data_pagamento' in self.params:
            attrs['data_pagamento'] = self.params.pop('data_pagamento')
        else:
            raise serializers.ValidationError({'error': f'Data do pagamento não informada. '})

        if 'dia_vencimento' in self.params:
            attrs['dia_vencimento'] = self.params.pop('dia_vencimento')
        else:
            raise serializers.ValidationError({'error': f'Dia do vencimento não informada. '})

        attrs['cliente'] = Empresa()

        for item in self.params:
            attrs[item] = self.params[item]

        attrs['tipo_pagamento'] = 'febraban'

        return attrs

    def to_representation(self, instance):

        self._get_builder()
        builder = self.builder(self.validated_data)
        adapter = builder.build(self.validated_data['contratos'])

        processo = self.processo()
        processo.geracao(adapter, self.validated_data['conta'].codigo_banco)

        ret = OrderedDict()
        ret['file'] = processo.exportacao()
        ret['name_file'] = f'ACC.{datetime.date.today().strftime("%d%m%Y")}.123456.123456.REM'

        return ret
