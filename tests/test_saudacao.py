import unittest
from src.saudacao import saudacao


class TestSaudacao(unittest.TestCase):
    def test_nome(self):
        self.assertIn('UFPR', saudacao('UFPR'))

    def test_vazio(self):
        with self.assertRaises(ValueError):
            saudacao('   ')


if __name__ == '__main__':
    unittest.main()
