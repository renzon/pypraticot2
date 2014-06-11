import unittest


def soma(param, param1):
    return param + param1


class BasicoTests(unittest.TestCase):
    def test_soma(self):
        resultado = soma(1, 2)
        self.assertEqual(3, resultado)
        resultado = soma(3, 2)
        self.assertEqual(5, resultado)


if __name__ == '__main__':
    unittest.main()
