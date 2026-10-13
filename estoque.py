class estoque:
    def __init__(self, produto, quantidade=0):
        self.produto = produto
       
        if quantidade < 0:
            self.quantidade = 0
        else:
         self.quantidade - quantidade 
   
    def adicionar(self, qtd):
            if qtd > 0:
                if qtd <= self.quantidade:
                    self.quantidade = self.quantidade + qtd
    
    def remover(self, qtd):
            if qtd <= self.quantidade:
                self.quantidade = self.quantidade - qtd
   
    def consultar_quantidade (self):
            print("produto:", {self.produto}, "| estoque:", {self.quantidade})