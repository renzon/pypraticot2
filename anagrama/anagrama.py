import unittest


def sao_anagramas(frase1, frase2):
    """
    Funcao que identifica anagramas
    :param frase1:
    :param frase2:
    :return: True se frase1 e frase2 sao anagramas e False caso contrario
    """

    # eliminar espacos em branco
    frase1 = frase1.replace(' ', '')
    frase2 = frase2.replace(' ', '')

    # comparar tamanho de cadeia com letras. Se for diferente, nao sao anagramas
    if len(frase1) != len(frase2):
        return False

    # remover cada letra de frase1 de frase2, uma a uma da para fazer isso com
    # dica: parar remover apenas uma lestra, utilize frase2.replate('a','',1)



class AnagramaTests(unittest.TestCase):
    def test_anagramas(self):
        self.assertTrue(sao_anagramas('aba', 'baa'))
        self.assertTrue(sao_anagramas('aba', 'aba'))
        self.assertTrue(sao_anagramas('the alias men', 'alan smithee'))

    def test_nao_anagramas(self):
        self.assertFalse(sao_anagramas('not the alias men', 'alan smithee'))
        self.assertFalse(sao_anagramas('aba', 'abab'))
        self.assertFalse(sao_anagramas('aba', 'abb'))