from datetime import date

class Operacao:
    def __init__(self, cpf: str, codigo: int):
        self.data = date.today()
        self.cpf = cpf
        self.codigo = codigo
        self.ativo = bool()

    def get_data(self):
        return self.data

    def set_data(self, data: date):
        self.data = data

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo: int):
        self.codigo = codigo

    def get_ativo(self):
        return self.ativo

    def set_ativo(self, ativo: True):
        self.ativo = ativo

