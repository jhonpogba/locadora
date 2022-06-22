from datetime import datetime
from sqlite3 import Date


class Operacao:
    def __init__(self, cpf: str, codigo: str):
        self.data = Date
        self.cpf = cpf
        self.codigo = codigo
        self.ativo = True

    def get_data(self):
        return self.data

    def set_data(self, data: Date):
        self.data = data

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo: str):
        self.codigo = codigo

    def get_ativo(self):
        return self.ativo

    def set_ativo(self, ativo: True):
        self.ativo = ativo

