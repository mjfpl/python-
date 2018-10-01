__author__ = 'computer'
import unittest
from Lemon.class_09_17_test.MathMethod import MathMethod
class class_Test(unittest.TestCase):
    def test_sum(self):
        t = MathMethod()
        sum = t.Sum(1,2)
        print('两个数相加的值为：{}'.format(sum))

    def test_sub(self):
        t = MathMethod()
        t.Sub(1,2)
        # print('两个数相加的值为：{}'.format(sub))
    su = unittest.s