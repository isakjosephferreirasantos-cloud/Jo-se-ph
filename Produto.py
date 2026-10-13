class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_produto(self):
        print(f"produto: {self.nome}|preco: {self.preco:.2f}")

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco*(percentual/100)


