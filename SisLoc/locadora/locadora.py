from SisLoc.Cadatrar.cliente import Cliente
from SisLoc.Cadatrar.filme import Filme
from SisLoc.Cadatrar.reserva import Reserva
from SisLoc.Repositorio.repositorio_cliente import RepositorioCliente
from SisLoc.Repositorio.repositorio_filme import RepositorioFilme
from SisLoc.Repositorio.repositorio_operacao import RepositoriOperacao


class Locadora:
    def __init__(self, clientes: RepositorioCliente, filmes: RepositorioFilme, operacoes: RepositoriOperacao):
        self.filmes = filmes
        self.clientes = clientes
        self.operacao = operacoes

    def cadastrarCliente(self,cliente: Cliente):
        self.clientes.cadastrar(cliente)

    def buscarCliente(self,cpf:str):
        return  self.clientes.buscar(cpf)

    def atualizarCadastroCliente(self,cliente: Cliente):
        self.clientes.atualizar(cliente)

    def removerCliente(self,cpf: str):
        if self.operacao.numeroLocacoesAtivas(cpf) == 0:
            self.clientes.deletar(cpf)

    def cadastrarFilme(self,filme: Filme):
        self.filmes.cadastrar(filme)

    def buscarFilme(self,codigo:int):
        return self.filmes.buscar(codigo)

    def atualizarCadastroFilme(self,filme: Filme):
        self.filmes.atualizar(filme)

    def removerFilme(self,codigo: int):
        if self.operacao.numeroLocacoesAtivas(codigo) == 0:
            self.filmes.deletar(codigo)

    def reservarFilme(self,cpf: str, codigo: int):
        reserva = Reserva(cpf, codigo)
        if self.buscarCliente(cpf) is not None and self.buscarFilme(codigo) is not None and Filme.get_numeroCopias() == self.operacao.numeroLocacoes(cpf):
                self.operacao.cadastrar(reserva)


    def finalizarReservaFilme(self,cpf: str, codigo: int):
        filme = self.operacao.buscarReservas(cpf)
        if filme is not None:
            self.operacao.deletarReserva(cpf,codigo)

    def locarFilme(self, cpf: str, codigo: int):
        cliente = self.buscarCliente(cpf)
        filme = self.buscarFilme(codigo)
        if cliente is not None and filme is not None and RepositoriOperacao.numeroLocacoesAtivas(cpf) < Filme.get_numeroCopias() and not RepositoriOperacao.buscarReservas(cpf) is not None or RepositoriOperacao.buscarReservas(cpf) == cliente:
            RepositoriOperacao.cadastrar(cliente)

    def devolverFilme(self, cpf: str, codigo: int):
        cliente = self.buscarCliente(cpf)
        filme = self.buscarFilme(codigo)
        locacao = self.operacao.buscarLocacoes(cpf)
        if cliente is not None and filme is not None and locacao is not None:
            self.operacao.deletarReserva(cpf,codigo)


    def imprimirHistoricoLocacao(self,cpf: str):
        if self.buscarCliente(cpf) is not None:
            print(self.operacao.listarLocacoes(cpf))

    def imprimirFilmesMaisLocados(self, top: int):
        pass

