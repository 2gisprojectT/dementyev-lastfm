__author__ = 'devgen'

from unittest import TestCase
import unittest

from numbers import Numbers


class NumberTest(TestCase):
    def test_init(self):
        num = Numbers(1, 2, 3)
        self.assertEquals(1, num.a, "A wrong")
        self.assertEquals(2, num.b, "B wrong")
        self.assertEquals(3, num.c, "C wrong")

    def test_sum(self):
        num = Numbers(1, 2, 3)
        self.assertEquals(6, num.sum(), "Sum wrong")

    def test_multiplication(self):
        num = Numbers(2, -2, 3)
        self.assertEqual(-12, num.multiplication(), "Multiply wrong")


    def test_abs_multiplication(self):
        num = Numbers(2, -2, 3)
        self.assertEqual(float(12.0), num.abs_multiplication(), "Abs multiply wrong")


if __name__ == '__main__':
    unittest.main()
