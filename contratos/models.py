
class LeiauteFBBBase(object):
    numero_sequencial_arquivo = '1'


class LeiauteFBBBradesco(LeiauteFBBBase):
    numero_convenio = ''
    versao_arquivo = ''
    versao_lote = ''

class LeiauteFBBCEF(LeiauteFBBBase):
    numero_convenio = ''
    versao_arquivo = ''
    versao_lote = ''
    ambiente_cliente = ''
    transmissao = ''
    compromisso = ''
    tipo_compromisso = ''


class LeiauteFBBBancoBrasil(LeiauteFBBBase):
    numero_convenio = ''
    versao_arquivo = ''
    versao_lote = ''
    forma_lancamento = ''


class Conta(object):
    codigo_banco = '107'
    nome_banco = 'BRADESCO'
    numero_agencia = ''
    digito_agencia = ''
    numero_conta = ''
    digito_conta = ''
    tipo_conta = ''

    leiaute_fbb_brad = LeiauteFBBBradesco()
    leiaute_fbb_cef = LeiauteFBBCEF()
    leiaute_fbb_bb = LeiauteFBBBancoBrasil()


class Empresa(object):
    cnpj = ''
    razao = ''
    cep = ''
    logradouro = ''
    logradouro_numero = ''
    cidade = ''
    uf = ''


class Contrato(object):
    cpf = ''
    nome = ''
    cep = ''
    logradouro = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''
    uf = ''

    liquido = 10000.00

    conta = Conta()

