'''
Created on Apr 7, 2020

@author: Diwakar
'''
import unittest
import calculator

class test_Calculator(unittest.TestCase):
            
    def test_Add(self):
        self.assertEqual(calculator.add(10, 2), 12)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-5, 4), -1)
        self.assertRaises(TypeError, calculator.add, 'something')
#
    def test_Subtract(self):
        self.assertEqual(calculator.subtract(10, 2), 8)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-5, -4), -1)
        self.assertRaises(TypeError, calculator.subtract, 'subtract')
#
    def test_Multiply(self):
        self.assertEqual(calculator.multiply(3, 2), 6)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-5, -4), 20)
#
    def test_Divide(self):
        self.assertEqual(calculator.divide(10,2), 5)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-6, -2), 3)
        
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(4,0)
#
    def test_Exponent(self):
        self.assertEqual(calculator.exponent(10,2), 100)
        self.assertEqual(calculator.exponent(10,1), 10)
        self.assertEqual(calculator.exponent(10,0), 1)
        self.assertEqual(calculator.exponent(1,0), 1)
        self.assertRaises(TypeError, calculator.exponent, 'watch the values')


if __name__ == "__main__":
    unittest.main()
