
class LeiauteFBBBase(object):
    numero_sequencial_arquivo = '1'
    forma_lancamento = '01'
    versao_arquivo = '089'


class LeiauteFBBBradesco(LeiauteFBBBase):
    numero_convenio = '141251'
    versao_lote = ''


class LeiauteFBBCEF(LeiauteFBBBase):
    numero_convenio = '654789'
    versao_lote = ''
    ambiente_cliente = ''
    transmissao = ''
    compromisso = ''
    tipo_compromisso = ''


class LeiauteFBBBancoBrasil(LeiauteFBBBase):
    numero_convenio = '123456'
    versao_lote = ''


class Conta(object):
    codigo_banco = '107'
    nome_banco = 'BRADESCO'
    numero_agencia = '0731'
    digito_agencia = ' '
    numero_conta = '1905709'
    digito_conta = '7'
    tipo_conta = '1'

    leiaute_fbb_brad = LeiauteFBBBradesco()
    leiaute_fbb_cef = LeiauteFBBCEF()
    leiaute_fbb_bb = LeiauteFBBBancoBrasil()


class Empresa(object):
    cnpj = '43339622000151'
    razao = 'Empresa Teste Informática ME'
    cep = '60356620'
    logradouro = 'Vila Dona Branca'
    logradouro_numero = '682'
    cidade = 'Fortaleza'
    uf = 'CE'


class Contrato(object):
    cpf = '83410871977'
    nome = 'Nelson Davi Santos'
    cep = '49075040'
    logradouro = 'Vila Amapá'
    numero = '431'
    complemento = ''
    bairro = 'Siqueira Campos'
    cidade = 'Aracaju'
    uf = 'SE'
    liquido = 10000.00
    conta = Conta()

