import unittest
from classes import ClassForTest


class TestForClasses(unittest.TestCase):

    def setUp(self):
        self.classTest = ClassForTest(2, 4)

    def test_class_dif(self):
        self.assertEqual(self.classTest.check_dif(), -2)

    def test_class_sum(self):
        self.assertEqual(self.classTest.check_sum(), 6)
