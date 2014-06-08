class Operacao():
    def calcular(self, param1, param2):
        pass


class Adicao(Operacao):
    def calcular(self, param1, param2):
        return param1 + param2


class Subtracao(Operacao):
    def calcular(self, param1, param2):
        return param1 - param2


class Calculadora():
    def __init__(self):
        self.sinal_de_operacao = None
        self.param1 = None
        self.param2 = None
        self.operacoes = {}

    def adicionar_operacao(self, sinal_de_operacao, operacao):
        self.operacoes[sinal_de_operacao] = operacao

    def calcular_resultado(self):
        operacao_escolhida = self.operacoes[self.sinal_de_operacao]
        resultado = operacao_escolhida.calcular(self.param1, self.param2)
        return resultado

    def obter_input(self):
        self.sinal_de_operacao = input('Digite o sinal da operação')
        self.param1 = float(input('Digite o primeiro parametro'))
        self.param2 = float(input('Digite o segundo parametro'))


if __name__ == '__main__':
    calculadora = Calculadora()
    adicao = Adicao()
    calculadora.adicionar_operacao('+', adicao)

    calculadora.obter_input()
    print(calculadora.calcular_resultado())