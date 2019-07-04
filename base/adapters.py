
def get_value_fk(instance, field_name, fks_name=[]):
    if len(fks_name) == 0:
        ret = getattr(instance, field_name)
        return ret if ret else ''
    for fk_name in fks_name:
        fks_name.remove(fk_name)
        instance_local = getattr(instance, fk_name)

        if not instance_local:
            return ''

        return get_value_fk(instance_local, field_name, fks_name)


class PagamentoOnlineAdapter(object):

    def __init__(self, dados_entrada, contratos):
        self.servidores_adapter = []
        self.entidade_numero_inscricao = get_value_fk(dados_entrada['cliente'], 'cnpj').replace('.', '').replace('-', '').replace('/', '')
        self.entidade_razao_social = get_value_fk(dados_entrada['cliente'], 'razao')
        self.entidade_endereco_logradouro = get_value_fk(dados_entrada['cliente'], 'logradouro_entidade')
        self.entidade_endereco_numero = get_value_fk(dados_entrada['cliente'], 'log_numero_entidade')
        self.entidade_endereco_complemento = ''
        self.entidade_endereco_cidade = get_value_fk(dados_entrada['cliente'], 'nome', ['cidade_entidade'])
        self.entidade_endereco_cep = get_value_fk(dados_entrada['cliente'], 'cep_entidade').replace('.', '').replace('-', '')
        self.entidade_endereco_cep_complemento = ''
        self.entidade_endereco_uf = get_value_fk(dados_entrada['cliente'], 'sigla', ['uf_entidade'])

        self.convenio_conta_agencia_banco_codigo = dados_entrada['conta'].convenio_agencia.banco.codigo
        self.convenio_conta_agencia_banco_nome = dados_entrada['conta'].convenio_agencia.banco.descricao
        self.convenio_conta_agencia_codigo = dados_entrada['conta'].convenio_agencia.numero_agencia
        self.convenio_conta_agencia_digito = dados_entrada['conta'].convenio_agencia.digito
        self.convenio_conta_codigo = dados_entrada['conta'].numero_conta
        self.convenio_conta_digito = dados_entrada['conta'].digito
        self.convenio_conta_nsa = dados_entrada['numero_sequencial_arquivo']
        self.data_pagamento = dados_entrada['data_pagamento'].replace('/', '')


class ServidorPagamentoAdapter(object):

    def __init__(self, contrato):
        self.banco = get_value_fk(contrato, 'banco')
        self.agencia = get_value_fk(contrato, 'agencia')
        self.agencia_digito = get_value_fk(contrato, 'dv_agencia')
        self.conta = get_value_fk(contrato, 'conta')
        self.conta_digito = get_value_fk(contrato, 'dv_conta')
        self.tipo_conta = get_value_fk(contrato, 'tipo_conta')
        self.liquido = contrato.liquido
        self.nome = get_value_fk(contrato, 'nome')
        self.cpf = get_value_fk(contrato, 'cpf').replace('.', '').replace('-', '')
        self.logradouro = get_value_fk(contrato, 'logradouro')
        self.numero = get_value_fk(contrato, 'numero')
        self.complemento = get_value_fk(contrato, 'complemento')
        self.bairro = get_value_fk(contrato, 'bairro')
        self.cidade = get_value_fk(contrato, 'nome', ['cidade'])
        self.cep = get_value_fk(contrato, 'cep').replace('.', '').replace('-', '')
        self.estado = get_value_fk(contrato, 'uf')
        self.valor_pagamento = self.liquido
