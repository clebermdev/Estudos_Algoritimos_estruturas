class Produto:
    def __init__(self, nome, preco = 10.00, qtd = 0):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        
        def __str__(self):
        txt = "Produto: " +self.nome
        txt += "\n preco: " + str(self.preco)
        return txt    