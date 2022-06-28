from SisLoc.Cadatrar.cliente import Cliente


class RepositoriCliente:
    def __init__(self):
        self.clientes = [None] * 100
        self.indice = 0

    def cadatrar(self, cliente: Cliente):
        self.clientes[self.indice] = cliente
        self.indice += 1

    def buscar(self, cpf: str):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.clientes[i].get_CPF() == cpf:
                achou = True
            else:
                i += 1
        if achou is True:
            return self.clientes[i]
        else:
            return None

    def atualizar(self, cliente: Cliente):
        for i in self.clientes:
            if cliente == self.clientes[i]:
                pass
            else:
                return None
