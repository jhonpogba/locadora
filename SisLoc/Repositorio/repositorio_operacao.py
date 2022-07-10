from SisLoc.Cadatrar.locacao import Locacao
from SisLoc.Cadatrar.operacao import Operacao
from SisLoc.Cadatrar.reserva import Reserva


class RepositoriOperacao:
    def __init__(self):
        self.operacoes = []

    def cadastrar(self, operacao: Operacao):
        if operacao not in self.operacoes:
            self.operacoes.append(operacao)
            operacao.set_ativo(True)
        else:
            print('Operacao ja cadastrada!!')

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
        locacao = self.listarLocacoes(cpf)
        return len(locacao)

    def numeroLocacoes(self, codigo: int):
        locacoes = []
        for locacao in self.operacoes:
            if locacao.get_codigo() == codigo and isinstance(locacao, Locacao):
                locacoes.append(locacao)
        return len(locacoes)

    def numeroLocacoesAtivas(self, cpf: str):
        locacoes = []
        for locacao in self.operacoes:
            if locacao.get_codigo() == cpf and locacao.get_ativo() is True and isinstance(locacao, Locacao):
                locacoes.append(locacao)
        return len(locacoes)

    def numeroLocacoesAtivas(self, codigo: int):
        locacoes = []
        for locacao in self.operacoes:
            if locacao.get_codigo() == codigo and locacao.get_ativo() is True and isinstance(locacao, Locacao):
                locacoes.append(locacao)
        return len(locacoes)

    def numeroReservas(self, codigo: int):
        reservas = []
        for reserva in self.operacoes:
            if reserva.get_codigo() == codigo and reserva.get_ativo() is True and isinstance(reserva, Reserva):
                reservas.append(reserva)
        return len(reservas)

