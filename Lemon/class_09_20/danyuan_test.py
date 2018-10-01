__author__ = 'computer'
import unittest
# 这个类来继承 Testcase 来写用例
from Lemon.class_09_20.test_math import Math
class TestAdd(unittest.TestCase):
    def test_two_sum(self):
        m = Math()
        res = m.sum(1,2)
        print('测试结果{}'.format(res))

    def test_two_sum1(self):
        m = Math()
        res = m.sum(-1,-2)
        print('测试结果{}'.format(res))

    def test_two_sum2(self):
        m = Math()
        res = m.sum(0,0)
        print('测试结果{}'.format(res))


if __name__ == '__main__':
    unittest.main()
    # 调用这个main函数 会默认执行所有用例
