class Pessoa(object):

    def __init__(self, data=None):
        if data:
            self.id = data[0]
            self.nome = data[1]
            self.sobrenome = data[2]
            self.idade = data[3]
            self.endereco = Endereco(data)

    def load_json(self, dict_pessoa):
        self.id = dict_pessoa['id']
        self.nome = dict_pessoa['nome']
        self.sobrenome = dict_pessoa['sobrenome']
        self.idade = dict_pessoa['idade']

        self.endereco = Endereco()
        self.endereco.load_json(dict_pessoa['endereco'])


class Endereco(object):
    
    def __init__(self, data=None):
        if data:
            self.id = data[4]
            self.logradouro = data[5]
            self.cidade = data[6]
            self.uf = data[7]

    def load_json(self, dict_pessoa):
        self.id = dict_pessoa['id']
        self.logradouro = dict_pessoa['logradouro']
        self.cidade = dict_pessoa['cidade']
        self.uf = dict_pessoa['uf']
