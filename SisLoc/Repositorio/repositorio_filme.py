from SisLoc.Cadatrar.filme import Filme


class RepositorioFilme:

    def __init__(self):
        self.filmes = []

    def cadastrar(self, filme: Filme):
        if self.buscar(filme.get_codigo())is None:
            self.filmes.append(filme)
        else:
            print('Filme não cadastrado!')

    def buscar(self, codigo: int):
        for filme in self.filmes:
            if filme.get_codigo() == codigo:
                return filme
        return None

    def atualizar(self, filme: Filme):
        filme = self.buscar(filme.get_codigo())
        if filme is not None:
            filme.set_titulo(filme.get_titulo)
            filme.set_genero(filme.get_genero)
            filme.set_dataLancamento(filme.get_dataLancamento)
            filme.set_direto(filme.get_direto)
            filme.set_sinopse(filme.get_sinopse)
            filme.set_produtores(filme.get_produtores)
            filme.set_precoLocacao(filme.get_precoLocacao)
            filme.set_numeroCopias(filme.get_numeroCopias)
        else:
            print('Filme não encontrado!')

    def deletar(self, codigo: int):
        for filme in self.filmes:
            if filme.get_codigo() == codigo:
                self.filmes.pop(self.filmes.index(filme))

    def listar(self):
        return self.filmes

