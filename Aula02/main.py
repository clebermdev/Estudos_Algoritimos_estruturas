from Pessoa import Pessoa
from Produto import Produto
from Cidade import Cidade


c1 = Cidade ()
c2 = Cidade ("Porto Alegre")

p1 = Pessoa ("João")
p2 = Pessoa ("Maria", cid = c1 )


prod01 = Produto("Coca Cola", 9.90)
prod01 = Produto("Pepsi", qtd = 50)
prod01 = Produto("Fanta", 7.85, 30)

ped = Pedido ( cli = p2)

