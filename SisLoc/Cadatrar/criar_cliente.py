from SisLoc.Cadatrar.cliente import Cliente
from SisLoc.Cadatrar.filme import Filme
from SisLoc.Cadatrar.operacao import Operacao


class CriarCliente:

    if __name__ == '__main__':
        #Cadastrar um cliente
        cliente = Cliente('083.664.993-16')
        cliente.set_nome('Jonnathan')
        cliente.set_endereco('Vila Fonseca, nº23')
        cliente.imprimir()

        # Cadastrar filmes
        filmes = Filme(2,'eu')
        filmes.set_atores(['bet','joa'])
        filmes.set_direto('caio')
        filmes.set_genero('acao')
        filmes.set_produtores('te')
        filmes.set_precoLocacao(2.45)
        filmes.set_numeroCopias(5)
        filmes.set_codigo(2)
        filmes.set_sinopse('isso')
        filmes.set_titulo('eu')
        filmes.imprimir()

        # Testa operacao
        op = Operacao('083.664.993-16',2)
        op.set_ativo(True)
        print(op.get_ativo())

