import unittest
from unittest.mock import patch
from functions import check_after_sum, check_dif, division, return_dict
from check_sum import check_sum


class TestFunctions(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(check_sum(1, 2), 3)

    def test_dif(self):
        self.assertEqual(check_dif(4, 2), 2)

    def test_division(self):
        self.assertRaises(ZeroDivisionError, division, 5, 0)
        self.assertEqual(division(6, 3), 2)

    @patch("functions.check_sum")
    def test_with_mock(self, mockCheckSum):
        mockCheckSum.return_value = 5
        self.assertEqual(check_after_sum(5, 2), 35)
        self.assertEqual(check_after_sum(6,2), 40)

    def test_key(self):
        self.assertIn("a", return_dict())

    if __name__ == '__main__':
        unittest.main()
