from datetime import datetime

from SisLoc.Cadatrar.cliente import Cliente
from SisLoc.Cadatrar.filme import Filme
from SisLoc.Cadatrar.locacao import Locacao
from SisLoc.Cadatrar.operacao import Operacao
from SisLoc.Cadatrar.reserva import Reserva
from SisLoc.Repositorio.repositorio_cliente import RepositorioCliente
from SisLoc.Repositorio.repositorio_filme import RepositorioFilme
from SisLoc.Repositorio.repositorio_operacao import RepositoriOperacao
from SisLoc.locadora.locadora import Locadora

cliente = Cliente('1234567')
cliente.set_nome('Wendel')
cliente.set_endereco('Rua das Flores, 145')
cliente1 = Cliente('3456789')
cliente1.set_nome('Jordan')
cliente1.set_endereco('Bell air, 15')
a = RepositorioCliente()
a.cadastrar(cliente)
a.cadastrar(cliente1)
cliente.set_nome("Joanderson")
print(a)
a.deletar('1234567')
print(a)
uso = Operacao('1020304050', 10)
print(uso.get_data())
data1 = '{:%d/%m/%Y}'.format(datetime(year=2004, month=4, day=14))
uso.set_data(data1)
print(uso.get_data())

filme = Filme(15, 'O amor')
data = '{:%d/%m/%Y}'.format(datetime(year=2009, month=10, day=20))
filme.set_dateLancamento(data)
filme.set_genero(['romance','acao'])
filme.set_direto('Keanu Reeves')
filme.set_atores(['Johnny Depp','paulo'])
filme.set_sinopse('Um filme que encanta todos que assistem , sem classificacao indicativa')
filme.set_numeroCopias(5)
b = RepositorioFilme()
b.cadastrar(filme)
op = Reserva('124578963',1)
op1 = Reserva('11122244478', 10)
op4 = Locacao('012345678', 2)
op5 = Locacao('456789123', 3)



hist = RepositoriOperacao()
hist.cadastrar(op4)
hist.cadastrar(op5)
hist.cadastrar(op)
hist.cadastrar(op1)
print(hist)
hist.buscarReservas('124578963')
hist.buscarLocacoes('012345678')
locacao = Locacao('1234567', 2)
locadora = Locadora(a, b, hist)
locadora.reservarFilme('1234567', 2)
locadora.imprimirHistoricoLocacoes('1234567')