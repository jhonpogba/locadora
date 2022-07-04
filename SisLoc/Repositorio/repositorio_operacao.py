from SisLoc.Cadatrar.operacao import Operacao


class RepositoriOperacao:
    def __init__(self):
        self.operacoes = []

    def cadastrar(self, operacao: Operacao):
        pass

    def buscarReservas(self, cpf: str):
        pass

    def buscarLocacoes(self, cpf: str):
        pass

    def deletarReserva(self, cpf: str, codigo: int):
        pass

    def deletarLocacao(self, cpf: str, codigo: int):
        pass

    def listarLocacoes(self, cpf: str):
        pass

    def numeroLocacoes(self, cpf: str):
        pass

    def numeroLocacoesAtivas(self, cpf: str):
        pass

    def numeroLocacoes(self, codigo: int):
        pass

    def numeroReservas(self, codigo: int):
        pass

