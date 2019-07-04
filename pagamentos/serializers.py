import datetime
from abc import ABCMeta
from collections import OrderedDict

from rest_framework import serializers

from febraban import builders
from febraban.processos import ProcessoPagamentoFebraban


class PagamentoOnlineSerializer(serializers.Serializer, metaclass=ABCMeta):

    @staticmethod
    def _clear_prefix(data):
        attrs = {}

        prefixs = ['lpbf_', 'lpcf_', 'lpbbf_']

        for prefix in prefixs:
            for index, item in data.items():
                if prefix in index:
                    attrs[index.replace(prefix, '')] = data.get(index)

        return attrs

    def _get_processo_pagamento(self):
        if self.validated_data['tipo_pagamento'] == 'febraban':
            self.processo = ProcessoPagamentoFebraban

    def _get_builder(self):
        if self.validated_data['conta'].convenio_agencia.banco.codigo == '107':
            self.builder = builders.PagamentoOnlineFBBBradescoBuilder
        elif self.validated_data['conta'].convenio_agencia.banco.codigo == '104':
            self.builder = builders.PagamentoOnlineFBBCEFBuilder
        elif self.validated_data['conta'].convenio_agencia.banco.codigo == '001':
            self.builder = builders.PagamentoOnlineFBBBancoBrasilBuilder

        self._get_processo_pagamento()

    def validate(self, attrs):
        data = self.context['request'].data['params']

        attrs = self._clear_prefix(data)
        # attrs['contratos'] = self.context['contratos']

        return attrs

    def to_representation(self, instance):

        self._get_builder()
        builder = self.builder(self.validated_data)
        adapter = builder.build(self.validated_data['contratos'])

        processo = self.processo()
        processo.geracao(adapter, self.validated_data['conta'].convenio_agencia.banco.codigo)

        ret = OrderedDict()
        ret['file'] = processo.exportacao()
        ret['name_file'] = f'ACC.{datetime.date.today().strftime("%d%m%Y")}.123456.123456.REM'

        return ret
