class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_dados(self):
        print(f"ola, meu nome é {self.nome} e tenho {self.idade}")

