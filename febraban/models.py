#
# campos duplicados nas classes por conta da exportação que usa a ordem dos campos do modelo
#


class Febraban:
    def __init__(self):
        self.header = None
        self.lotes = []
        self.trailler = TrailerArquivo()
        self.sequencial_lote = 0


class HeaderArquivo:
    def __init__(self):
        self.codigo_banco_compensacao = None
        self.lote_servico = '0000'
        self.tipo_registro = '0'
        self.uso_exclusivo_febraban = ''.rjust(9)
        self.tipo_inscricao_empresa = '2'
        self.numero_inscricao_empresa = None


class HeaderArquivoBradesco(HeaderArquivo):
    def __init__(self):
        super().__init__()

        self.codigo_convenio_banco = None
        self.agencia_mantenedora_conta = None
        self.digito_verificador_agencia = None
        self.numero_conta_corrente = None
        self.digito_verificador_conta = None
        self.digito_verificador_ag_conta = ' '
        self.nome_empresa = None
        self.nome_banco = None
        self.uso_exclusivo_febraban_dois = ''.rjust(10)
        self.codigo_remessa_retorno = '1'
        self.data_geracao_arquivo = None
        self.hora_geracao_arquivo = None
        self.numero_sequencial_arquivo = None
        self.numero_versao_layout_arquivo = '089'
        self.densidade_gravacao_arquivo = '01600'
        self.para_uso_reservado_banco = ''.rjust(20)
        self.para_uso_reservado_empresa = ''.rjust(20)
        self.uso_exclusivo_febraban_tres = ''.rjust(29)


class HeaderArquivoCEF(HeaderArquivo):
    def __init__(self):
        super().__init__()

        self.codigo_convenio_banco = None
        self.parametro_transmissao = None
        self.ambiente_cliente = None
        self.ambiente_caixa = ' '
        self.origem_aplicativo = '   '
        self.numero_versao = '0000'
        self.filler = '   '
        self.agencia_mantenedora_conta = None
        self.digito_verificador_agencia = None
        self.numero_conta_corrente = None
        self.digito_verificador_conta = None
        self.digito_verificador_ag_conta = ' '
        self.nome_empresa = None
        self.nome_banco = None
        self.filler2 = ''.rjust(10)
        self.codigo_remessa_retorno = '1'
        self.data_geracao_arquivo = None
        self.hora_geracao_arquivo = None
        self.numero_sequencial_arquivo = None
        self.numero_versao_layout_arquivo = '089'
        self.densidade_gravacao_arquivo = '01600'
        self.para_uso_reservado_banco = ''.rjust(20)
        self.para_uso_reservado_empresa = ''.rjust(20)
        self.uso_exclusivo_febraban_filler = ''.rjust(11)
        self.ident_cobranca = '   '
        self.uso_exclusivo_van = '000'
        self.tipo_servico = '  '
        self.ocorrencia_cod_sem_papel = ''.rjust(10)


class HeaderArquivoBancoBrasil(HeaderArquivo):
    def __init__(self):
        super().__init__()

        self.numero_convenio = None
        self.codigo_convenio = '0126'
        self.uso_reservado_banco = '     '
        self.arquivo_teste = '  '
        self.agencia_mantenedora_conta = None
        self.digito_verificador_agencia = None
        self.numero_conta_corrente = None
        self.digito_verificador_conta = None
        self.digito_verificador_ag_conta = ' '
        self.nome_empresa = None
        self.nome_banco = None
        self.filler2 = ''.rjust(10)
        self.codigo_remessa_retorno = '1'
        self.data_geracao_arquivo = None
        self.hora_geracao_arquivo = None
        self.numero_sequencial_arquivo = None
        self.numero_versao_layout_arquivo = '089'
        self.densidade_gravacao_arquivo = '01600'
        self.para_uso_reservado_banco = ''.rjust(19)
        self.para_uso_reservado_empresa = ''.rjust(20)
        self.ident_cobranca = '   '
        self.uso_exclusivo_van = '000'
        self.tipo_servico = '00'
        self.ocorrencia_cod_sem_papel = '0'.zfill(10)


class LoteArquivo:
    def __init__(self):
        self.header = None
        self.detalhe_segmentos = []
        self.trailler = TrailerLote


class DetalheSegmentos:
    def __init__(self):
        self.detalhe_segmento_a = DetalheSegmentoA
        self.detalhe_segmento_b = DetalheSegmentoB


class HeaderLote:
    def __init__(self):
        self.codigo_banco_compensacao = None
        self.lote_servico = '0001'
        self.tipo_registro = '1'
        self.tipo_operacao = 'C'
        self.tipo_servico = '30'
        self.forma_lancamento = None
        self.numero_versao_layout_lote = '045'
        self.uso_exclusivo_febraban = ' '
        self.tipo_inscricao_empresa = '2'
        self.numero_inscricao_empresa = None


class HeaderLoteCEF(HeaderLote):
    def __init__(self):
        super().__init__()

        self.codigo_convenio_banco = None
        self.tipo_compromisso = None
        self.codigo_compromisso = None
        self.parametro_transmissao = None
        self.filler = ' '.rjust(6)
        self.agencia_mantenedora_conta = None
        self.digito_verificador_agencia = None
        self.numero_conta_corrente = None
        self.digito_verificador_conta = None
        self.digito_verificador_agconta = ' '
        self.nome_empresa = None
        self.mensagem = ''.rjust(40)
        self.logradouro = None
        self.numero = None
        self.complemento = None
        self.cidade = None
        self.cep = None
        self.complemento_cep = None
        self.estado = None
        self.uso_exclusivo_febraban_filler = ''.rjust(8)
        self.codigo_ocorrencias_retorno = ''.rjust(10)


class HeaderLoteBancoBrasil(HeaderLote):
    def __init__(self):
        super().__init__()

        self.numero_convenio = None
        self.codigo_convenio = '0126'
        self.uso_reservado_banco = '     '
        self.arquivo_teste = '  '
        self.agencia_mantenedora_conta = None
        self.digito_verificador_agencia = None
        self.numero_conta_corrente = None
        self.digito_verificador_conta = None
        self.digito_verificador_agconta = ' '
        self.nome_empresa = None
        self.mensagem = ''.rjust(40)
        self.logradouro = None
        self.numero = None
        self.complemento = None
        self.cidade = None
        self.cep = None
        self.complemento_cep = None
        self.estado = None
        self.uso_exclusivo_febraban_filler = ''.rjust(8)
        self.codigo_ocorrencias_retorno = ''.rjust(10)


class HeaderLoteBradesco(HeaderLote):
    def __init__(self):
        super().__init__()

        self.codigo_convenio_banco = None
        self.agencia_mantenedora_conta = None
        self.digito_verificador_agencia = None
        self.numero_conta_corrente = None
        self.digito_verificador_conta = None
        self.digito_verificador_agconta = ' '
        self.nome_empresa = None
        self.mensagem = ''.rjust(40)
        self.logradouro = None
        self.numero = None
        self.complemento = None
        self.cidade = None
        self.cep = None
        self.complemento_cep = None
        self.estado = None
        self.indicativo_forma_pagamento_servico = '01'
        self.uso_exclusivo_febraban_cnab = ''.rjust(6)
        self.codigo_ocorrencias_retorno = None


class DetalheSegmentoA:
    def __init__(self):
        self.codigo_banco_compensacao = None
        self.lote_servico = '0001'
        self.tipo_registro = '3'
        self.numero_sequencial_registro_lote = None
        self.codigo_segmento_reg_detalhe = 'A'
        self.tipo_movimento = '0'
        self.codigo_instrucao_movimento = '00'
        self.codigo_camara_centralizadora = None
        self.codigo_banco_favorecido = None
        self.agencia_mantenedora_cta_favor = None
        self.digito_verificador_agencia = ''
        self.numero_conta_corrente = None
        self.digito_verificador_conta = None
        self.digito_verificador_agconta = ' '
        self.nome_favorecido = None
        self.numero_doc_atribuido_empresa = None


class DetalheSegmentoABradesco(DetalheSegmentoA):
    def __init__(self):
        super().__init__()

        self.data_pagamento = None
        self.tipo_moeda = 'BRL'
        self.quantidade_moeda = '0'.zfill(15)
        self.valor_pagamento = None
        self.numero_doc_atribuido_banco = ' '.ljust(20)
        self.data_real_efetivacao_pagto = '00000000'
        self.valor_real_efetivacao_pagto = '0'.zfill(15)
        self.outras_informacoes = ' '.ljust(40)
        self.complemento_tipo_servico = '  '
        self.codigo_finalidade_ted = '     '
        self.complemento_finalidade_pagto = '  '
        self.uso_exclusivo_febraban = ' '.rjust(3)
        self.aviso_favorecido = '0'
        self.codigos_ocorrencias_retorno = ' '.rjust(10)


class DetalheSegmentoACEF(DetalheSegmentoA):
    def __init__(self):
        super().__init__()

        self.filler = ''.ljust(13)
        self.tipo_conta = '1'
        self.data_vencimento = None
        self.tipo_moeda = 'BRL'
        self.quantidade_moeda = '0'.zfill(15)
        self.valor_lancamento = None
        self.numero_doc_atribuido_banco = '0'.zfill(9)
        self.filler2 = '   '
        self.quantidade_parcelas = '01'
        self.indicador_bloqueio = 'N'
        self.indicador_forma_parcelamento = None
        self.periodo_dia_vencimento = None
        self.numero_parcela = '00'
        self.data_efetivacao = '0'.zfill(8)
        self.valor_real_efetivacao = '0'.zfill(15)
        self.informacao2 = ' '.ljust(40)
        self.finalidade_doc = '00'
        self.uso_febraban = ''.ljust(10)
        self.aviso_favorecido = '0'
        self.ocorrencias = ''.ljust(10)


class DetalheSegmentoABancoBrasil(DetalheSegmentoA):
    def __init__(self):
        super().__init__()

        self.data_pagamento = None
        self.tipo_moeda = 'BRL'
        self.quantidade_moeda = '0'.zfill(15)
        self.valor_pagamento = None
        self.numero_doc_atribuido_banco = '0'.zfill(20)
        self.data_efetivacao = '0'.zfill(8)
        self.valor_real_efetivacao = '0'.zfill(15)
        self.informacao2 = ' '.ljust(40)
        self.complemento_tipo_servico = '00'
        self.finalidade_ted = '     '
        self.finalidade_complementar = '  '
        self.uso_febraban = '   '
        self.aviso = '0'
        self.ocorrencias = ''.ljust(10)


class DetalheSegmentoB:
    def __init__(self):
        self.codigo_banco_compensacao = None
        self.lote_servico = '0001'
        self.tipo_registro = '3'
        self.numero_sequencial_registro_lote = None
        self.codigo_segmento_reg_detalhe = 'B'
        self.uso_exclusivo_febraban = ''.rjust(3)
        self.tipo_inscricao_favorecido = '1'
        self.numero_inscricao_favorecido = None
        self.logradouro = None
        self.numero = None
        self.complemento = None
        self.bairro = None
        self.cidade = None
        self.cep = None
        self.complemento_cep = None
        self.estado = None
        self.data_vencimento = None
        self.valor_documento = None
        self.valor_abatimento = '0'.zfill(15)
        self.valor_desconto = '0'.zfill(15)
        self.valor_mora = '0'.zfill(15)
        self.valor_multa = '0'.zfill(15)
        self.codigo_doc_favorecido = ''.rjust(15)
        self.aviso_favorecido = '0'
        self.uso_exclusivo_siape = '000000'
        self.codigo_ispb = '00000000'


class TrailerLote:
    def __init__(self):
        self.codigo_banco_compensacao = None
        self.lote_servico = '0001'
        self.tipo_registro = '5'
        self.uso_exclusivo_febraban = ''.rjust(9)
        self.quantidade_registros_lote = None
        self.somatoria_valores = None
        self.somatoria_quantidade_moedas = '0'.zfill(18)
        self.numero_aviso_debito = '0'.zfill(6)
        self.uso_exclusivo_febraban_dois = ' '.ljust(165)
        self.codigos_ocorrencias_retorno = ' '.ljust(10)


class TrailerArquivo:
    def __init__(self):
        self.codigo_banco_compensacao = None
        self.lote_servico = '9999'
        self.tipo_registro = '9'
        self.uso_exclusico_febraban = ' '.rjust(9)
        self.quantidade_lotes_arquivo = None
        self.quantidade_registros_arquivo = None
        self.quantidade_contas_conc = '0'.zfill(6)
        self.uso_exclusivo_febraban_dois = ' '.rjust(205)
