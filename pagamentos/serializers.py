import datetime
from collections import OrderedDict
from rest_framework import serializers

from contratos.models import Conta, Empresa
from febraban import builders
from febraban.processos import ProcessoPagamentoFebraban

# TODO - Kayo Riccelo: estes dados vem do frontend conforme as configurações do usuario
params = {
    'conta': Conta(),
    'data_pagamento': '01/07/2016',
    'dia_vencimento': '05',
    'ambiente_cliente': '',
    'camara_centralizadora': '',
    'forma_parcelamento_pagto': '',
    'forma_lancamento': '',
    'tipo_compromisso': ''
}


class PagamentoOnlineSerializer(serializers.Serializer):

    def _get_processo_pagamento(self):
        if self.validated_data['tipo_pagamento'] == 'febraban':
            self.processo = ProcessoPagamentoFebraban

    def _get_builder(self):
        if self.validated_data['conta'].banco == '107':
            self.builder = builders.PagamentoOnlineFBBBradescoBuilder
        elif self.validated_data['conta'].banco == '104':
            self.builder = builders.PagamentoOnlineFBBCEFBuilder
        elif self.validated_data['conta'].banco == '001':
            self.builder = builders.PagamentoOnlineFBBBancoBrasilBuilder

        self._get_processo_pagamento()

    def validate(self, attrs):
        attrs['contratos'] = self.context['contratos']

        if 'conta' in params:
            attrs['conta'] = params.pop('conta')
        else:
            raise serializers.ValidationError({'error': 'Conta não encontrada.'})

        if 'data_pagamento' in params:
            attrs['data_pagamento'] = params.pop('data_pagamento')
        else:
            raise serializers.ValidationError({'error': f'Data do pagamento não informada. '})

        if 'dia_vencimento' in params:
            attrs['dia_vencimento'] = params.pop('dia_vencimento')
        else:
            raise serializers.ValidationError({'error': f'Dia do vencimento não informada. '})

        attrs['cliente'] = Empresa()

        for item in params:
            attrs[item] = params[item]

        return attrs

    def to_representation(self, instance):

        self._get_builder()
        builder = self.builder(self.validated_data)
        adapter = builder.build(self.validated_data['contratos'])

        processo = self.processo()
        processo.geracao(adapter, self.validated_data['conta'].banco)

        ret = OrderedDict()
        ret['file'] = processo.exportacao()
        ret['name_file'] = f'ACC.{datetime.date.today().strftime("%d%m%Y")}.123456.123456.REM'

        return ret
