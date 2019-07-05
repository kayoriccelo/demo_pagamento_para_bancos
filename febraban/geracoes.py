import datetime
import locale

from base.utils import remover_acentos
from .choices import *
from .models import *


class GeracaoFebraban(object):

    def __init__(self):
        self.tipo_febraban = None
        self.adapter = None
        self.arquivo = None
        self.formas_lancamento = ['01', '02', '03', '04', '05']
        self.sequencial_lote = 0
        self.sequencial_total = 0
        self.somatoria_valores = 0

    def _criar_header_arquivo(self):

        def cef(dados):
            header = HeaderArquivoCEF()
            header.codigo_convenio_banco = dados.convenio_conta_leiaute_cef_numero_convenio.zfill(6)
            header.parametro_transmissao = dados.convenio_conta_leiaute_cef_transmissao.zfill(2)
            header.ambiente_cliente = dados.convenio_conta_leiaute_cef_ambiente_cliente.rjust(1)

            return header

        def banco_brasil(dados):
            header = HeaderArquivoBancoBrasil()
            header.numero_convenio = dados.convenio_conta_leiaute_bb_numero_convenio[0:9].zfill(9)

            return header

        def bradesco(dados):
            header = HeaderArquivoBradesco()
            header.codigo_convenio_banco = dados.convenio_conta_leiaute_brad_numero_convenio.ljust(20)

            if dados.convenio_conta_leiaute_brad_versao_lote == '045':
                header.numero_versao_layout_arquivo = '089'
            else:
                header.numero_versao_layout_arquivo = '080'

            return header

        header_dict = {
            CEF: cef,
            BANCO_BRASIL: banco_brasil,
            BRADESCO: bradesco
        }

        header = header_dict[self.tipo_febraban](self.adapter)

        header.codigo_banco_compensacao = self.adapter.convenio_conta_agencia_banco_codigo.zfill(3)
        header.numero_inscricao_empresa = self.adapter.entidade_numero_inscricao.zfill(14)
        header.agencia_mantenedora_conta = self.adapter.convenio_conta_agencia_codigo.zfill(5)
        header.digito_verificador_agencia = self.adapter.convenio_conta_agencia_digito.rjust(1)
        header.numero_conta_corrente = self.adapter.convenio_conta_codigo.zfill(12)
        header.digito_verificador_conta = self.adapter.convenio_conta_digito.zfill(1)
        header.nome_empresa = remover_acentos(self.adapter.entidade_razao_social[0:30].ljust(30))
        header.nome_banco = remover_acentos(self.adapter.convenio_conta_agencia_banco_nome[0:30].ljust(30))
        header.data_geracao_arquivo = self.adapter.data_pagamento.zfill(8)
        header.hora_geracao_arquivo = datetime.datetime.now().strftime('%H%M%S')

        header.numero_sequencial_arquivo = self.adapter.convenio_conta_nsa.zfill(6)

        return header

    def _criar_header_lote(self, forma_lancamento):

        def cef(dados):
            header = HeaderLoteCEF()
            header.codigo_convenio_banco = dados.convenio_conta_leiaute_cef_numero_convenio.zfill(6)
            header.tipo_compromisso = dados.convenio_conta_leiaute_cef_tipo_compromisso.zfill(2)
            header.codigo_compromisso = dados.convenio_conta_leiaute_cef_compromisso.zfill(4)
            header.paramentro_transmissao = dados.convenio_conta_leiaute_cef_transmissao.rjust(2)
            header.numero_versao_layout_lote = dados.convenio_conta_leiaute_cef_versao_lote.zfill(3)
            return header

        def banco_brasil(dados):
            header = HeaderLoteBancoBrasil()
            header.numero_convenio = dados.convenio_conta_leiaute_bb_numero_convenio[0:9].zfill(9)
            header.numero_versao_layout_lote = dados.convenio_conta_leiaute_bb_versao_lote.zfill(3)
            return header

        def bradesco(dados):
            header = HeaderLoteBradesco()
            header.codigo_convenio_banco = dados.convenio_conta_leiaute_brad_numero_convenio.ljust(20)
            # header.numero_versao_layout_lote = dados.convenio_conta_leiaute_brad_versao_lote.zfill(3)

            if header.numero_versao_layout_lote == '045':
                header.uso_exclusivo_febraban_cnab = '1'

            return header

        header_dict = {
            CEF: cef,
            BANCO_BRASIL: banco_brasil,
            BRADESCO: bradesco
        }

        header_lote = header_dict[self.tipo_febraban](self.adapter)
        header_lote.codigo_banco_compensacao = self.arquivo.header.codigo_banco_compensacao
        header_lote.forma_lancamento = forma_lancamento.zfill(2)
        header_lote.tipo_inscricao_empresa = self.arquivo.header.tipo_inscricao_empresa.zfill(1)
        header_lote.numero_inscricao_empresa = self.arquivo.header.numero_inscricao_empresa.zfill(14)
        header_lote.agencia_mantenedora_conta = self.arquivo.header.agencia_mantenedora_conta.zfill(5)
        header_lote.digito_verificador_agencia = self.arquivo.header.digito_verificador_agencia.rjust(1)
        header_lote.numero_conta_corrente = self.arquivo.header.numero_conta_corrente.zfill(12)
        header_lote.digito_verificador_conta = self.arquivo.header.digito_verificador_conta.rjust(1)
        header_lote.digito_verificador_agconta = self.arquivo.header.digito_verificador_ag_conta.rjust(1)
        header_lote.nome_empresa = remover_acentos(self.arquivo.header.nome_empresa.ljust(30))
        header_lote.logradouro = remover_acentos(self.adapter.entidade_endereco_logradouro.ljust(30))
        header_lote.numero = self.adapter.entidade_endereco_numero.zfill(5)
        header_lote.complemento = remover_acentos(self.adapter.entidade_endereco_complemento.ljust(15))
        header_lote.cidade = remover_acentos(self.adapter.entidade_endereco_cidade.ljust(20))
        header_lote.cep = self.adapter.entidade_endereco_cep[0:5].zfill(5)
        header_lote.complemento_cep = self.adapter.entidade_endereco_cep[5:8].zfill(3)
        header_lote.estado = self.adapter.entidade_endereco_uf.rjust(2)

        self.sequencial_total += 1

        return header_lote

    def _criar_detalhe_segmento(self, servidor):
        detalhe_segmento = DetalheSegmentos()
        detalhe_segmento.detalhe_segmento_a = self._criar_detalhe_segmento_a(servidor)
        detalhe_segmento.detalhe_segmento_b = self._criar_detalhe_segmento_b(servidor)
        return detalhe_segmento

    def _criar_detalhe_segmento_a(self, servidor):

        def cef(dados):
            detalhe = DetalheSegmentoACEF()
            detalhe.numero_doc_atribuido_empresa = dados.convenio_conta_leiaute_cef_numero_convenio.zfill(6)
            detalhe.data_vencimento = self.arquivo.header.data_geracao_arquivo
            detalhe.valor_lancamento = str(locale.currency(
                servidor.valor_pagamento, grouping=True, symbol=None).replace('.', '').replace(',', '')).zfill(15)
            detalhe.indicador_forma_parcelamento = servidor.indicador_forma_parcelamento.zfill(1)
            detalhe.periodo_dia_vencimento = dados.periodo_dia_vencimento.zfill(2)

            return detalhe

        def banco_brasil(dados):
            detalhe = DetalheSegmentoABancoBrasil()
            detalhe.numero_doc_atribuido_empresa = dados.convenio_conta_leiaute_bb_numero_convenio.zfill(20)
            detalhe.data_pagamento = self.arquivo.header.data_geracao_arquivo
            detalhe.valor_pagamento = str(locale.currency(
                servidor.valor_pagamento, grouping=True, symbol=None).replace('.', '').replace(',', '')).zfill(15)

            return detalhe

        def bradesco(dados):
            detalhe = DetalheSegmentoABradesco()
            detalhe.numero_doc_atribuido_empresa = dados.convenio_conta_leiaute_brad_numero_convenio
            detalhe.data_pagamento = self.arquivo.header.data_geracao_arquivo
            detalhe.valor_pagamento = str(locale.currency(
                servidor.valor_pagamento, grouping=True, symbol=None).replace('.', '').replace(',', '')).zfill(15)

            return detalhe

        detalhe_dict = {
            CEF: cef,
            BANCO_BRASIL: banco_brasil,
            BRADESCO: bradesco
        }

        detalhe_segmento_a = detalhe_dict[self.tipo_febraban](self.adapter)
        detalhe_segmento_a.codigo_banco_compensacao = self.arquivo.header.codigo_banco_compensacao

        detalhe_segmento_a.codigo_banco_favorecido = servidor.banco.zfill(3)
        detalhe_segmento_a.agencia_mantenedora_cta_favor = servidor.agencia.zfill(5)
        detalhe_segmento_a.digito_verificador_agencia = servidor.agencia_digito.zfill(1)
        detalhe_segmento_a.numero_conta_corrente = servidor.tipo_conta.zfill(3) + servidor.conta.zfill(9)
        detalhe_segmento_a.digito_verificador_conta = servidor.conta_digito.zfill(1)

        detalhe_segmento_a.nome_favorecido = remover_acentos(servidor.nome[0:30].ljust(30))

        if servidor.forma_lancamento == '05':
            detalhe_segmento_a.codigo_camara_centralizadora = '000'
        elif servidor.valor_pagamento >= 3000:
            detalhe_segmento_a.codigo_camara_centralizadora = '018'
        else:
            detalhe_segmento_a.codigo_camara_centralizadora = '700'

        if servidor.banco == self.arquivo.header.codigo_banco_compensacao:
            detalhe_segmento_a.complemento_tipo_servico = '06'

        self.somatoria_valores += servidor.valor_pagamento
        self.sequencial_lote += 1
        self.sequencial_total += 1
        detalhe_segmento_a.numero_sequencial_registro_lote = str(self.sequencial_lote).zfill(5)

        return detalhe_segmento_a

    def _criar_detalhe_segmento_b(self, servidor):
        detalhe_segmento_b = DetalheSegmentoB()
        detalhe_segmento_b.codigo_banco_compensacao = self.arquivo.header.codigo_banco_compensacao.zfill(3)
        detalhe_segmento_b.numero_inscricao_favorecido = servidor.cpf.zfill(14)
        detalhe_segmento_b.logradouro = remover_acentos(servidor.logradouro[0:30].ljust(30))
        detalhe_segmento_b.numero = servidor.numero.zfill(5)
        detalhe_segmento_b.complemento = servidor.complemento[0:14].rjust(15)
        detalhe_segmento_b.bairro = remover_acentos(servidor.bairro[0:14].ljust(15))
        detalhe_segmento_b.cidade = servidor.cidade[0:19].ljust(20)
        detalhe_segmento_b.cep = servidor.cep[0:5].zfill(5)
        detalhe_segmento_b.complemento_cep = servidor.cep[5:8].zfill(3)
        detalhe_segmento_b.estado = servidor.estado.ljust(2)
        detalhe_segmento_b.data_vencimento = self.adapter.data_pagamento
        detalhe_segmento_b.valor_documento = str(locale.currency(
            servidor.valor_pagamento, grouping=True, symbol=None).replace('.', '').replace(',', '')).zfill(15)

        self.somatoria_valores += servidor.valor_pagamento
        self.sequencial_lote += 1
        self.sequencial_total += 1

        detalhe_segmento_b.numero_sequencial_registro_lote = str(self.sequencial_lote).zfill(5)
        return detalhe_segmento_b

    def _criar_trailler_lote(self):
        trailler = TrailerLote()
        trailler.codigo_banco_compensacao = self.arquivo.header.codigo_banco_compensacao
        trailler.quantidade_registros_lote = str(self.sequencial_lote).zfill(6)
        trailler.somatoria_valores = str(locale.currency(self.somatoria_valores, grouping=True, symbol=None).replace(
            '.', '').replace(',', '')).zfill(18)

        self.sequencial_total += 1
        return trailler

    def _criar_trailler_arquivo(self):
        trailler = TrailerArquivo()
        trailler.codigo_banco_compensacao = self.arquivo.header.codigo_banco_compensacao
        trailler.quantidade_lotes_arquivo = str(len(self.arquivo.lotes)).zfill(6)
        trailler.quantidade_registros_arquivo = str(self.sequencial_total).zfill(6)
        return trailler

    def _criar_lotes(self):
        lotes = []

        for forma_lancamento in self.formas_lancamento:
            lote_arquivo = LoteArquivo()

            for servidor in self.adapter.servidores_adapter:
                if servidor.forma_lancamento == forma_lancamento:
                    lote_arquivo.detalhe_segmentos.append(self._criar_detalhe_segmento(servidor))

            if len(lote_arquivo.detalhe_segmentos) > 0:
                lote_arquivo.header = self._criar_header_lote(forma_lancamento)
                lote_arquivo.trailler = self._criar_trailler_lote()

                lotes.append(lote_arquivo)

        return lotes

    def gerar(self, arquivo, adapter, tipo_febraban):
        locale.setlocale(locale.LC_ALL, ('pt_BR', 'UTF-8'))
        self.tipo_febraban = tipo_febraban
        self.adapter = adapter

        self.arquivo = arquivo
        self.arquivo.header = self._criar_header_arquivo()

        self.arquivo.lotes = self._criar_lotes()

        self.arquivo.trailler = self._criar_trailler_arquivo()

        return self.arquivo
