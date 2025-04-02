from Pessoa import Pessoa
from Produto import Produto
from datetime import date

class Pedido:
    def __init__(self, data = date.today , cli = Pessoa ("Balcão")):
        self.id = None
        self.data = data
        self.cliente = cli
        self.produtos= []
        
    def addProd(self, prod):
        if prod !- None and prod.preco >= 10:
            self.produtos.append(prod)
        soma = 0.0
        for p in self.produtos:
            soma += p.preco
        return soma
    
    def __str__(self):
        txt - "Pedido Realizado em: " + Str (self.data)
        txt +- "\nCliente: " + str (self.cliente)   
        txt += "\nProdutos: "
        for p in self .produtos:
            txt += str(p)
            txt += "\n____________________________\n"
        return txt