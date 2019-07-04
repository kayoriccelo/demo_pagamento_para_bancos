from unicodedata import normalize


def remover_acentos(string):
    return normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII')
