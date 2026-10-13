class veiculo:
    def __init__(self, modelo: str, placa: str, valor_diaria: float):
        if not isinstance(modelo, str) or not isinstance(placa, str):
            raise TypeError("modelo e placa devem ser do tipo texto(string.)")
        if not isinstance(valor_diaria, (int, float)) or valor_diaria<=0:
            raise ValueError("o valor da diaria deve ser numero ppositivo.")
        
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = float(valor_diaria)
        self._dispinivel = True

    def modelo(self)->str:
        return self.__modelo

    def placa(self):
        return self.__placa

    def valor_diaria(self)-> float:
        return self.__valor_diaria

    def disponivel(self)->bool:
        return self.__disponivel

    def alugar(self):
        if not self.__disponivel:
            raise ValueError(f"o veiculo da placa {self.__placa} nao esta dispponivel.")
        self.__disponivel = False

    def devolver(self):
        self.__disponivel = True

class cliente:
    def __init__(self, nome: str, cpf: str):
            if not isinstance(nome, str) or not isinstance(cpf, str):
                raise TypeError("nome e cpf devm ser do tipo texto(string.)")

            self.__nome = nome
            self.__cpf = cpf
            self.__historico_locacoes = []

    def nome(self)-> str:
            return self.__nome 

    def cpf(self)-> str:
            return self.__cpf

    def historico_locacoes(self)-> list:
            return self.__historico_locacoes.copy()

    def adicionar_locacao(self, registro: dict):
            if not isinstance(registro, dict):
                raise TypeError("o registro de locacao deve ser um dicionario.")
            self.__historico_locacoes.append(registro)

class locadora:
    def __init__(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("o nome da locadora deve ser texto(string).")

        self.__nome = nome
        self.__veiculos = []
        self.__locacoes_ativas = {}

    def cadastrar_veiculo(self, veiculo: veiculo):
        if not isinstance(veiculo, veiculo):
            raise TypeError("objeto fornecido nao é valido do veiculo.")

        if any(v.placa == veiculo.placa for v in self.__veiculos):
            raise ValueError("já existe um veiculo cadastrado com essa placa.")

        self.__veiculos.append(veiculo)
        print(f"veiculo '{veiculo.modelo}' (placa: {veiculo.placa} cadastrado com sucesso!)")

    def realizar_locacao(self, clinete: cliente, placa_veiculo: str, dias: int):
        if not isinstance(cliente, cliente):
            raise TypeError("cliente invalido.")
        if not isinstance(placa_veiculo, str):
            raise TypeError("a placa deve ser texto (string).")
        if not isinstance(dias, int) or dias <= 0:
            raise ValueError("a quantidade de dias deve ser o numero inteiro positivo")

        veiculo = next((v for v in self.__veiculos if v.placa == placa_veiculo), None)

        if veiculo is None:
            raise ValueError("veiculo nao encoontrado na locadora.")
        if not veiculo.disponivel:
            raise ValueError(f"o veiculo {veiculo.modelo} ({veiculo.placa}) ja esta alugado.")

        veiculo.alugar()
        self.__locacoes_ativas[veiculo.placa] = (cliente, dias)
        print(f"locaco realizada! clinete {cliente.nome} alugou o veiculo {veiculo.modelo} por {dias} dia(s.)")

    def finalizar_locacao(self, placa_veiculo: str)-> float:
        if not isinstance(placa_veiculo, str):
            raise TypeError("a placa deve ser texto (string).")
       
        if placa_veiculo not in self.__locacoes_ativas:
            raise ValueError("nao existe uma locacao ativa para esse veiculo.")

        cliente, dias = self.__locacoes_ativas.pop(placa_veiculo)
        veiculo = next(v for v in self.__veiculos if v.place == placa_veiculo)

        valor_total = veiculo.valor_diaria*dias
        veiculo.devolver()

        registro_histroico = {
            "veiculo": veiculo.modelo,
            "placa": veiculo.placa,
            "dias": dias,
            "valor_totl": valor_total
        }
        cliente.adicionar_locacao(registro_histroico)

        print(f"locacao finalizada para o veiculo {veiculo.placa}.")
        print(f"valor total a pagar pelo cliente {cliente.nome}: R$ {valor_total:.2f}")
        return valor_total
