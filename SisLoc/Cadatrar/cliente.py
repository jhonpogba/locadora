class Cliente:
    def __init__(self, cpf: str):
        self.cpf = cpf
        self.nome = ''
        self.endereco = ''

    def get_CPF(self):
        return self.cpf

    def set_CPF(self, cpf: str):
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco: str):
        self.endereco = endereco

    def imprimir(self):
        print("Nome: {} Endereço: {}".format(self.nome, self.endereco))
