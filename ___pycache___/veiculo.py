class Veiculo:
    def __init__(self, marca):
        self.marca = marca
    def ligar(self):
        print("veiculo ligado!")

class Carro(Veiculo):
    def __init__(self, marca, portas):
        super().__init__(marca)
        self.portas = portas
    def ligar(self):
        print(f"carro {self.marca} ligado!")

