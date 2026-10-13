class Funcionario:
    def _init__(self, nome, cargo):
        super().__init__(nome)
        self.cargo = cargo

    def aprentar(self):
        print(f"sou {self.nome}, cargo: {self.cagro}")