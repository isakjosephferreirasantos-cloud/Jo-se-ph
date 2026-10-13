class Biblioteca:
   
    def __init__(self, livros_disponiveis, livros_nao):
        livros_disponiveis=5
        self.livros_disponiveis = livros_disponiveis
        self.livros_nao = livros_nao
        while livros_disponiveis < 5:
            livros_nao-=1

    