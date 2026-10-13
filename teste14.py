class ContaBancaria:
    def __init__(self,saldo_inicial):
      self.__saldo=saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
  
    def get_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
conta.depositar(500)

print(conta.get_saldo()) # r$ 1500