from SisLoc.Cadatrar.cliente import Cliente


class RepositorioCliente:
    def __init__(self):
        self.clientes = []

    def cadastrar(self, cliente: Cliente):
        if self.buscar(cliente.get_CPF()) is None:
            self.clientes.append(cliente)
        else:
            print('Cliente já existente! ')

    def buscar(self, cpf: str):
        for cliente in self.clientes:
            if cliente.get_CPF() == cpf:
                return cliente
        return None

    def atualizar(self, cliente: Cliente):
        cliente = self.buscar(cliente.get_CPF())
        if cliente is not None:
            cliente.set_nome(cliente.get_nome)
            cliente.set_endereco(cliente.get_endereco)
        else:
            print('Filme não encontrado! ')

    def deletar(self, cpf: str):
        for cliente in self.clientes:
            if cliente.get_CPF() == cpf:
                self.clientes.pop(self.clientes.index(cliente))

    def listar(self):
        return self.clientes
