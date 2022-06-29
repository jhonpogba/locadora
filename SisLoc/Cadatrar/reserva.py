from SisLoc.Cadatrar.operacao import Operacao


class Reserva(Operacao):
    def __init__(self, cpf:str,codigo:int,prioridade: int):
        super().__init__(cpf, codigo)
        self.prioridade = prioridade

    def get_prioridade(self):
        return self.prioridade

    def set_prioridade(self, prioridade: int):
        self.prioridade = prioridade


