from SisLoc.Cadatrar.operacao import Operacao


class Reserva(Operacao):
    def __init__(self, prioridade: int):
        super().__init__(self.cpf, self.codigo)
        self.prioridade = prioridade

    def get_prioridade(self):
        return self.prioridade

    def set_prioridade(self, prioridade: int):
        self.prioridade = prioridade


