class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        if self.saldo >=valor:
            self.saldo -= valor

    def consultar_saldo(self):
        print(f"conta de:{self.titular}: saldo: R${self.saldo}")

    def get_saldo(self):
        return self._saldo 
