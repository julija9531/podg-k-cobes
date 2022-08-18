import unittest
from parameterized import parameterized

from main import balance

FIXTURE = [
    ('(((([{}]))))', 'Сбалансированно'),
    ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
    ('{{[()]}}', 'Сбалансированно'),
    ('}{}', 'Несбалансированно'),
    ('{{[(])]}}', 'Несбалансированно'),
    ('[[{())}]', 'Несбалансированно')
]

class TestFunctions(unittest.TestCase):

    @parameterized.expand(FIXTURE)
    def test_balance(self, text, result):
        self.assertEqual(balance(text), result)