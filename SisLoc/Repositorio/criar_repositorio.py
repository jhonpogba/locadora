from SisLoc.Cadatrar.cliente import Cliente
from SisLoc.Cadatrar.filme import Filme
from SisLoc.Cadatrar.operacao import Operacao
from SisLoc.Repositorio.repositorio_cliente import RepositorioCliente
from SisLoc.Repositorio.repositorio_filme import RepositorioFilme
from datetime import datetime

from SisLoc.Repositorio.repositorio_operacao import RepositoriOperacao


class CriarCliente:

    if __name__ == '__main__':
        # Criar Clientes
        cliente0 = Cliente('083.664.993-16')
        cliente0.set_nome('jonnathan')
        cliente0.set_endereco('Vila Fonseca, 23')
        cliente1 = Cliente('086.489.457-45')
        cliente1.set_nome('Felipe')
        cliente1.set_endereco('Santa Cruz, 38')

        # Cadastrar Cliente
        cc = RepositorioCliente()
        cc.cadastrar(cliente0)
        cc.cadastrar(cliente1)
        cc.buscar('083.664.993-16')
        cc.deletar('485.496.256-45')
        cc.atualizar(cliente1)
        cc.listar()

        # CRIAR FILMES
        filme0 = Filme(4, 'sei la')
        data1 = '{:%d/%m/%Y}'.format(datetime(year=2000, month=11, day=30))
        filme0.set_dateLancamento(data1)
        filme0.set_genero(['romance','acao'])
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

        # CADASTRAR OS FILMES NO REPOSITORIO FILME
        rf = RepositorioFilme()
        rf.cadastrar(filme0)
        rf.cadastrar(filme1)
        rf.buscar(6)
        rf.deletar(2)
        rf.listar()

        # CRIAR OPERACAO
        op = Operacao('O83.664.993-16',2)
        op.set_data(data)
        op0 = Operacao('086.865.452-45',5)
        op0.set_data(data1)

        # FAZER UMA OPERACAO
        ro = RepositoriOperacao()
        ro.cadastrar(op)
        ro.cadastrar(op0)
        ro.buscarReservas('458.869.126-45')
        ro.buscarLocacoes('426.964.168-48')
        ro.deletarReserva('452.265.789-19',9)
        ro.deletarLocacao('496.789.265-78',5)
        ro.numeroLocacoes('456.789.128-45')
        ro.numeroLocacoesAtivas(5)
        ro.listarLocacoes('083.664.993-16')


