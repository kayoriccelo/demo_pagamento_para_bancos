
class ExportacaoFebraban:

    @staticmethod
    def _criar_linha(leiaute):
        linha = ''
        for key in [field for field in leiaute.__dir__() if field.find('__') == -1]:
            if leiaute.__getattribute__(key):
                linha += str(leiaute.__getattribute__(key))
        return linha

    def exportar(self, arquivo):
        lista = [self._criar_linha(arquivo.header)]
        for lote in arquivo.lotes:
            lista.append(self._criar_linha(lote.header))
            for detalhe_segmento in lote.detalhe_segmentos:
                lista.append(self._criar_linha(detalhe_segmento.detalhe_segmento_a))
                lista.append(self._criar_linha(detalhe_segmento.detalhe_segmento_b))
            lista.append(self._criar_linha(lote.trailler))
        lista.append(self._criar_linha(arquivo.trailler))
        return '\n'.join(map(str, lista))
