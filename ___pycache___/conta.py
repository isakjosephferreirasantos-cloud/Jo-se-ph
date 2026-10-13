class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def exibir_saldo(self):
        print(f"Saldo: R$ {self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, saldo, limite):
        super()._init_(saldo)
        self.limite = limite

    def exibir_saldo(self):
        saldo_total = self.saldo + self.limite
        print(f"Saldo disponível (saldo + limite): R$ {saldo_total:.2f}")


class ContaPoupanca(Conta):
    def __init__(self, saldo, taxa):
        super()._init_(saldo)
        self.taxa = taxa

    def render_juros(self):
        self.saldo += self.saldo*(self.taxa / 100)
        print(f"Juros aplicados! Novo saldo: R$ {self.saldo:.2f}")

    

cp = ContaPoupanca(2000, 5)
cp.exibir_saldo() 
cp.render_juros()  