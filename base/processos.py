class ProcessoPagamento(object):
    arquivo_class = None
    geracao_class = None
    exportacao_class = None
    _arquivo = None

    def get_arquivo(self):
        if not self._arquivo:
            self._arquivo = self.arquivo_class()
        return self._arquivo

    def exportacao(self):
        return self.exportacao_class().exportar(self.get_arquivo())
