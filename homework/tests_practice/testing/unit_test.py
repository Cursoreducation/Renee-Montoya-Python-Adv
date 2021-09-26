from unittest import TestCase
from tests.functions_to_test import Calculator


class TestCalc(TestCase):
    """ Testing calculator of functions """

    def test_add_001(self):
        self.assertEqual(Calculator.add(50, 150), 200)
        self.assertNotEqual(Calculator.add(50, 150), 100)
        self.assertIsInstance(Calculator.add(200, 300), int)

    def test_subtract_002(self):
        self.assertIsInstance(Calculator.subtract(300.0, 200), float)
        self.assertNotEqual(Calculator.subtract(20, 15), 50)
        self.assertEqual(Calculator.subtract(120, 20), 100)

    def test_multiply_003(self):
        with self.assertRaises(TypeError):
            Calculator.multiply('40', '3')

        assert 80 in [20, 40, 80]

        self.assertIn(80, [20, 40, 80])
        self.assertNotIsInstance(Calculator.multiply(40, 50), float)

    def test_divide_004(self):
        self.assertEqual(Calculator.divide(100, 10), 10)
        self.assertIsInstance(Calculator.add(400, 300), int)
        self.assertEqual(Calculator.divide(10, 10), 1)

""" Instruction. For a check the results of tests run command in terminal: 
    'python -m unittest test/uni_test.py'(*depend from location directory)
    or run file with method: '__name__=='__main__' which below."""

if __name__ == "__main__":
    TestCalc()
