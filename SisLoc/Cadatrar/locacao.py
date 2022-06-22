from SisLoc.Cadatrar.operacao import Operacao


class Locacao(Operacao):
    def __init__(self, periodo: int):
        super().__init__(self.cpf, self.codigo)
        self.periodo = periodo

    def get_periodo(self):
        return self.periodo

    def set_periodo(self, periodo: int):
        self.periodo = periodo
