import unittest


def soma(param, param1):
    return param+param1


class BasicoTests(unittest.TestCase):
    def soma_test(self):
        resultado=soma(1,2)
        self.assertEqual(3,resultado)
        resultado=soma(3,2)
        self.assertEqual(5,resultado)
