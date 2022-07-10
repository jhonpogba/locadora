from SisLoc.Cadatrar.cliente import Cliente
from SisLoc.Cadatrar.filme import Filme
from SisLoc.Cadatrar.operacao import Operacao
from SisLoc.Repositorio.repositorio_cliente import RepositorioCliente
from SisLoc.Repositorio.repositorio_filme import RepositorioFilme
from SisLoc.Repositorio.repositorio_operacao import RepositoriOperacao
from SisLoc.locadora.locadora import Locadora
from datetime import datetime


class CriarCliente:

    if __name__ == '__main__':
        '''print("1- Cadastrar Cliente \n 2- Buscar Cliente \n 3- Atualizar Cliente \n Remover Cliente \n 4- Cadastrar Filme \n 5- Buscar Filme \n 6- Atualizar cadastro Filme \n 7- Remover Filme \n 8- Reservar Filme \n 9- Finalizar reserva filme \n 10- Locar Filme \n 11- Devolver Filme \n 12- Imprimir Historico Filme \n 13- Imprimir Filme Mais Locados")
        menu = int(input("O que você quer fazer? "))'''
        # CRIAR CLIENTES
        cliente0 = Cliente('083.664.993-16')
        cliente0.set_nome('jonnathan')
        cliente0.set_endereco('Vila Fonseca, 23')
        cliente1 = Cliente('086.489.457-45')
        cliente1.set_nome('Felipe')
        cliente1.set_endereco('Santa Cruz, 38')

        # CRIAR FILMES
        filme0 = Filme(4, 'sei la')
        data1 = '{:%d/%m/%Y}'.format(datetime(year=2000, month=11, day=30))
        filme0.set_dateLancamento(data1)
        filme0.set_genero(['romance', 'acao'])
        filme0.set_direto('Joao')
        filme0.set_atores(['joca', 'gerra'])
        filme0.set_sinopse('Chama todo mundo pra assistir')
        filme0.set_numeroCopias(5)
        filme1 = Filme(4, 'sei la')
        data = '{:%d/%m/%Y}'.format(datetime(year=2009, month=10, day=20))
        filme1.set_dateLancamento(data)
        filme1.set_genero(['romance', 'acao'])
        filme1.set_direto('Keanu Reeves')
        filme1.set_atores(['Johnny Depp', 'paulo'])
        filme1.set_sinopse('Um filme que encanta todos que assistem , sem classificacao indicativa')
        filme1.set_numeroCopias(5)

        op = RepositorioCliente()
        cd = RepositorioFilme()
        ps = RepositoriOperacao()

        #if menu == 1:
        #elif menu == 2:

        #elif menu == 3:
        atu = Locadora(op,cd,ps)
        atu.cadastrarCliente(cliente1)
        atu.cadastrarCliente(cliente0)
        atu.buscarCliente('451.879.354-16')
        atu.atualizarCadastroCliente(cliente0)
        #elif menu == 4:
        atu.removerCliente('458.156.145-45')
        #elif menu == 5:
        atu.cadastrarFilme(filme0)
        atu.cadastrarFilme(filme1)
        atu.buscarFilme(5)
        #elif menu == 7:
        atu.atualizarCadastroFilme(filme0)
        #elif menu == 8:
        atu.removerFilme(2)
        #elif menu == 9:
        atu.reservarFilme('083.664.993-16',2)
        #elif menu == 10:
        atu.locarFilme('458.153.789-16',2)
        #elif menu == 11:
        atu.devolverFilme('083.664.993-16',2)
        #elif menu == 12:
        atu.imprimirHistoricoLocacao('083.664.993-16')
        #elif menu == 13:
        atu.imprimirFilmesMaisLocados(5)

