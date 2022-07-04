from SisLoc.Cadatrar.locacao import Locacao
from SisLoc.Cadatrar.operacao import Operacao
from SisLoc.Cadatrar.reserva import Reserva


class RepositoriOperacao:
    def __init__(self):
        self.operacoes = []

    def cadastrar(self, operacao: Operacao):
        self.operacoes.append(operacao)
        operacao.set_ativo(True)

    def buscarReservas(self, cpf: str):
        reservas = []
        for reserva in self.operacoes:
            if isinstance(reserva, Reserva) and reserva.get_cpf() == cpf and reserva.get_ativo() is True:
                reservas.append(reserva)
        return reservas

    def buscarLocacoes(self, cpf: str):
        locacoes = []
        for locacao in self.operacoes:
            if isinstance(locacao, Locacao) and locacao.get_ativo() == cpf and locacao.get_ativo is True:
                locacoes.append(locacao)
        return locacoes

    def deletarReserva(self, cpf: str, codigo: int):
        for reserva in self.operacoes:
            if isinstance(reserva, Reserva) and reserva.get_cpf() == cpf and reserva.get_codigo() == codigo and reserva.get_ativo() is True:
                reserva.set_ativo(False)

    def deletarLocacao(self, cpf: str, codigo: int):
        for locacao in self.operacoes:
            if isinstance(locacao, Locacao) and locacao.get_cpf() == cpf and locacao.get_codigo() == codigo and locacao.get_ativo() is True:
                locacao.set_ativo(False)

    def listarLocacoes(self, cpf: str):
        locacoes = []
        for locacao in self.operacoes:
            if isinstance(locacao, Locacao) and locacao.get_cpf() == cpf:
                locacoes.append(locacao)
        return locacoes

    def numeroLocacoes(self, cpf: str):
        pass

    def numeroLocacoesAtivas(self, cpf: str):
        pass

    def numeroLocacoes(self, codigo: int):
        pass

    def numeroReservas(self, codigo: int):
        pass

