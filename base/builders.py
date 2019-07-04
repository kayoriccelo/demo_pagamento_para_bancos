
class PagamentoOnlineBuilder(object):
    adapter_class = None
    adapter = None

    def __init__(self, dados_entrada):
        self.dados_entrada = dados_entrada

    def build(self, contratos):
        self.adapter = self.adapter_class(self.dados_entrada, contratos)

        return self.adapter
