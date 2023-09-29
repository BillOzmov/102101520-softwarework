import unittest
from tkinter import Tk
from calculator_science import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.calculator = Calculator()

    def tearDown(self):
        self.root.destroy()

    def test_addition(self):
        # 测试加法运算
        self.calculator.Click('2')
        self.calculator.Click('+')
        self.calculator.Click('3')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '5')

    def test_subtraction(self):
        # 测试减法运算
        self.calculator.Click('2')
        self.calculator.Click('-')
        self.calculator.Click('3')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '-1')

    def test_multiplication(self):
        # 测试乘法运算
        self.calculator.Click('22')
        self.calculator.Click('*')
        self.calculator.Click('30')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '660')

    def test_division(self):
        # 测试除法运算
        self.calculator.Click('21')
        self.calculator.Click('÷')
        self.calculator.Click('30')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '0.7')

    def test_power(self):
        # 测试幂运算
        self.calculator.Click('2')
        self.calculator.Click('^')
        self.calculator.Click('10')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '1024')

    def test_logarithm(self):
        # 测试对数函数
        self.calculator.Click('3')
        self.calculator.Click('lg')
        self.calculator.Click('100')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '6.0')

    def test_square_root(self):
        # 测试平方根函数
        self.calculator.Click('7')
        self.calculator.Click('√')
        self.calculator.Click('9')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '21.0')

    def test_error_divide_by_zero(self):
        # 测试除以零的错误
        self.calculator.Click('7')
        self.calculator.Click('÷')
        self.calculator.Click('0')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '错误')

    def test_triangle_functions(self):
        # 测试三角函数
        self.calculator.Click('sin')
        self.calculator.Click('3')
        self.calculator.Click('+')
        self.calculator.Click('1')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '1.1411')

    def test_pi(self):
        # 测试π
        self.calculator.Click('2')
        self.calculator.Click('π')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '6.2832')

    def test_e(self):
        # 测试e
        self.calculator.Click('e')
        self.calculator.Click('=')
        self.assertEqual(self.calculator.result_var.get(), '2.7183')

    def test_All_clear(self):
        # 测试清除功能
        self.calculator.Click('7')
        self.calculator.Click('arcsin')
        self.calculator.Click('π')
        self.calculator.All_Clear()
        self.assertEqual(self.calculator.result_var.get(), '0')


if __name__ == '__main__':
    unittest.main()
