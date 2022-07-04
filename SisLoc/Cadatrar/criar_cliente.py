from SisLoc.Cadatrar.cliente import Cliente
from SisLoc.Repositorio.repositorio_cliente import RepositoriCliente


class CriarCliente:

    if __name__ == '__main__':
        cpf = str(input("CPF: "))
        nome = str(input("Nome: "))
        endereco = str(input("Endereco: "))
        cliente = Cliente(cpf)
        cliente.set_nome(nome)
        cliente.set_endereco(endereco)

        cliente.imprimir()
        cliente = RepositoriCliente()
        print(cliente.buscar('254'))


