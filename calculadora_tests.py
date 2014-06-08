import unittest
from calculadora import Adicao, Subtracao, Calculadora


class OperacaoTests(unittest.TestCase):
    def testar_adicao(self):
        adicao = Adicao()
        resultado = adicao.calcular(1, 2)
        self.assertEqual(3, resultado)

    def testar_subtracao(self):
        subtracao = Subtracao()
        resultado = subtracao.calcular(1, 2)
        self.assertEqual(-1, resultado)


class OperacaoMock(object):
    pass


class OperacoMockComResultado(object):
    def __init__(self):
        self.executou = 0

    def calcular(self, param1, param2):
        self.executou += 1
        return param2 * param1


class CalculadoraTests(unittest.TestCase):
    def adicionar_operacoes_test(self):
        calculadora = Calculadora()
        operacao = OperacaoMock()
        calculadora.adicionar_operacao('+', operacao)
        self.assertDictEqual({'+': operacao}, calculadora.operacoes)
        subtracao = OperacaoMock()
        calculadora.adicionar_operacao('-', subtracao)
        self.assertDictEqual({'+': operacao, '-': subtracao}, calculadora.operacoes)

    def calcular_resultado_test(self):
        calculadora = Calculadora()
        calculadora.param1 = 5
        calculadora.param2 = 4
        calculadora.sinal_de_operacao = '$'
        operacao_mock = OperacoMockComResultado()
        calculadora.adicionar_operacao('$', operacao_mock)
        resultado = calculadora.calcular_resultado()
        self.assertEqual(1, operacao_mock.executou)
        self.assertEqual(20, resultado)

        calculadora.param1 = 6
        calculadora.param2 = 4

        resultado = calculadora.calcular_resultado()
        self.assertEqual(2, operacao_mock.executou)
        self.assertEqual(24, resultado)

