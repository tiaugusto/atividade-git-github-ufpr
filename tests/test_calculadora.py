import unittest
from src.calculadora import somar, subtrair


class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(3, 4), 7)

    def test_subtrair(self):
        self.assertEqual(subtrair(4, 3), 1)


if __name__ == '__main__':
    unittest.main()
