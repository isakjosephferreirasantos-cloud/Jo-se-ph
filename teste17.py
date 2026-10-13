class Carro:
    def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

    def exibir_Dados(self):
             print(f"meu caarro é {self.marca}, o modelo é {self.modelo}, seu ano é {self.ano}")

c1 = Carro("fiat", "uno", 2002)
c2 = Carro("gtr", "r34", 1999)

c1.exibir_dados()
c2.exibir_dados()