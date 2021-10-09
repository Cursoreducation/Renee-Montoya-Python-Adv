from unittest.mock import patch
from unittest import TestCase
from functions_to_test import Calculator


class TestCalculator(TestCase):

    @patch.object(Calculator, return_value=4, attribute='add')
    def test_add_test(self,*args,**kwargs):
        self.assertEqual(Calculator.add(4, 2),4)



