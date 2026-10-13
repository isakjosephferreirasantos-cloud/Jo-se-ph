class contaBancaria:
    def _unit_(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
         if self.saldo >= valor:
            self.saldlo -= valor

c1 = contaBancaria("maria", 1000)
c1.depositar(500)
print(f"saldo de {c1.titular}: r${c1.saldo}")