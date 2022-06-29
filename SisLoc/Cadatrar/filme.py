from sqlite3 import Date


class Filme:
    def __init__(self,codigo: int, titulo: str):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = []
        self.dataLancamento = Date
        self.diretor = ''
        self.atores = []
        self.sinopse = ''
        self.produtores = []
        self.precoLocacao = float
        self.numeroCopias = int


    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo: int):
        self.codigo = codigo

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo: str):
        self.titulo = titulo

    def get_genero(self):
        return self.genero

    def set_genero(self, genero: []):
        self.genero = genero

    def get_dataLancamento(self):
        return self.dataLancamento

    def set_dateLancamento(self, dataLancamento: Date):
        self.dataLancamento = dataLancamento

    def get_direto(self):
        return self.diretor

    def set_direto(self, diretor: str):
        self.diretor = diretor

    def get_atores(self):
        return self.atores

    def set_atores(self, atores: []):
        self.atores = atores

    def get_sinopse(self):
        return self.sinopse

    def set_sinopse(self, sinopse: str):
        self.sinopse = sinopse

    def get_produtores(self):
        return self.produtores

    def set_produtores(self, produtores: []):
        self.produtores = produtores

    def get_precoLocacao(self):
        return self.precoLocacao

    def set_precoLocacao(self, precoLocacao: float):
        self.precoLocacao = precoLocacao

    def get_numeroCopias(self):
        return self.numeroCopias

    def set_numeroCopias(self, numeroCopias: int):
        self.numeroCopias = numeroCopias

    def imprimir(self):
        print("Código: {} Título: {} Gênero: {} Data de Lançamento: {} Atores: {} Diretor: {} Sinopse: {}".
              format(self.codigo,self.titulo,self.genero,self.dataLancamento,self.atores,self.diretor,self.sinopse))

