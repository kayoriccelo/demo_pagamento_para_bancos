from base.processos import ProcessoPagamento
from febraban.exportacoes import ExportacaoFebraban
from febraban.geracoes import GeracaoFebraban
from febraban.models import Febraban


class ProcessoPagamentoFebraban(ProcessoPagamento):
    arquivo_class = Febraban
    geracao_class = GeracaoFebraban
    exportacao_class = ExportacaoFebraban

    def geracao(self, adapter, tipo_febraban):
        self.geracao_class().gerar(self.get_arquivo(), adapter, tipo_febraban)
