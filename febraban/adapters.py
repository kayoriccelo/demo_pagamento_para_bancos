from base.adapters import PagamentoOnlineAdapter, get_value_fk, ServidorPagamentoAdapter


class PagamentoOnlineFBBBradescoAdapter(PagamentoOnlineAdapter):

    def __init__(self, dados_entrada, contratos):
        super(PagamentoOnlineFBBBradescoAdapter, self).__init__(dados_entrada, contratos)
        self.convenio_conta_leiaute_brad_numero_convenio = dados_entrada['numero_convenio']
        self.convenio_conta_leiaute_brad_versao_arquivo = dados_entrada['versao_arquivo']
        self.convenio_conta_leiaute_brad_versao_lote = dados_entrada['versao_lote']

        for contrato in contratos:
            self.servidores_adapter.append(ServidorPagamentoFBBBradescoAdapter(contrato))


class PagamentoOnlineFBBCEFAdapter(PagamentoOnlineAdapter):

    def __init__(self, dados_entrada, contratos):
        super(PagamentoOnlineFBBCEFAdapter, self).__init__(dados_entrada, contratos)
        self.convenio_conta_leiaute_cef_numero_convenio = dados_entrada['numero_convenio']
        self.convenio_conta_leiaute_cef_versao_arquivo = dados_entrada['versao_arquivo']
        self.convenio_conta_leiaute_cef_versao_lote = dados_entrada['versao_lote']
        self.convenio_conta_leiaute_cef_ambiente_cliente = dados_entrada['ambiente_cliente'].codigo
        self.convenio_conta_leiaute_cef_transmissao = dados_entrada['transmissao']
        self.convenio_conta_leiaute_cef_compromisso = dados_entrada['compromisso']
        self.convenio_conta_leiaute_cef_tipo_compromisso = dados_entrada['tipo_compromisso'].codigo
        self.periodo_dia_vencimento = dados_entrada['dia_vencimento']

        for contrato in contratos:
            self.servidores_adapter.append(ServidorPagamentoFBBCEFAdapter(contrato))


class PagamentoOnlineFBBBancoBrasilAdapter(PagamentoOnlineAdapter):

    def __init__(self, dados_entrada, contratos):
        super(PagamentoOnlineFBBBancoBrasilAdapter, self).__init__(dados_entrada, contratos)
        self.convenio_conta_leiaute_bb_numero_convenio = dados_entrada['numero_convenio']
        self.convenio_conta_leiaute_bb_versao_arquivo = dados_entrada['versao_arquivo']
        self.convenio_conta_leiaute_bb_versao_lote = dados_entrada['versao_lote']
        self.periodo_dia_vencimento = dados_entrada['dia_vencimento']

        for contrato in contratos:
            self.servidores_adapter.append(ServidorPagamentoFBBBancoBrasilAdapter(contrato))


class ServidorPagamentoFBBBradescoAdapter(ServidorPagamentoAdapter):

    def __init__(self, contrato):
        super(ServidorPagamentoFBBBradescoAdapter, self).__init__(contrato)

        self.forma_lancamento = get_value_fk(contrato, 'forma_lancamento')


class ServidorPagamentoFBBCEFAdapter(ServidorPagamentoAdapter):

    def __init__(self, contrato):
        super(ServidorPagamentoFBBCEFAdapter, self).__init__(contrato)

        self.forma_lancamento = get_value_fk(contrato, 'forma_lancamento')
        self.numero_doc_atribuido_empresa = get_value_fk(contrato, 'convenio_leiaute_pagto_cef_fbb_numero_convenio')
        self.indicador_forma_parcelamento = get_value_fk(
            contrato, 'convenio_leiaute_pagto_cef_fbb_forma_lancamento_codigo')


class ServidorPagamentoFBBBancoBrasilAdapter(ServidorPagamentoAdapter):

    def __init__(self, contrato):
        super(ServidorPagamentoFBBBancoBrasilAdapter, self).__init__(contrato)

        self.forma_lancamento = get_value_fk(contrato, 'convenio_leiaute_pgto_bb_fbb_forma_lancamento')
        self.numero_doc_atribuido_empresa = get_value_fk(contrato, 'convenio_leiaute_pgto_bb_fbb_numero_convenio')
