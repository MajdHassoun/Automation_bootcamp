import unittest
import unittest
from math_function import is_even
from math_function import modulo_func
from math_function import sum_function
from math_function import sub_function
from math_function import mul_function
from math_function import div_function


class TestMathFunction(unittest.TestCase):

    def test_is_even_true(self):
        # Arrange
        num = 4  # Mock

        # Act
        result = is_even(num)

        # Assert
        self.assertTrue(result)

    # Coverage - I did unit test for the True result. So also i should do for the False result.
    def test_is_even_false(self):
        # Arrange
        num = 3  # Mock

        # Act
        result = is_even(num)

        # Assert
        self.assertFalse(result)

    def test_modulo_function_zero(self):
        self.assertEqual(0, modulo_func(4), "The function not working well.")
        # self.assertEqual(Expected, Actual, msg)

    def test_sum_function_result(self):
        self.assertEqual(12, sum_function(8, 4), "the sum function isn't working")

    def test_sum_function_oneNeg(self):
        self.assertEqual(-10, sum_function(-13, 3), "the sum function isn't working")

    def test_sum_function_twoNeg(self):
        self.assertEqual(-12, sum_function(-8, -4), "the sum function isn't working")

    def test_sum_function_twoZero(self):
        self.assertEqual(0, sum_function(0, 0), "the sum function isn't working")

    def test_sum_function_numZero(self):
        self.assertEqual(5, sum_function(5, 0), "the sum function isn't working")

    def test_sum_function_char(self):
        self.assertEqual(5, sum_function(5, 'f'), "wrong input has been inserted")

    def test_sub_function_result(self):
        self.assertEqual(8, sub_function(12, 4), "the sum function isn't working")

    def test_sub_function_Neg(self):
        self.assertEqual(-1, sub_function(4, 5), "the sum function isn't working")

    def test_sub_function_twoNeg(self):
        self.assertEqual(-4, sub_function(-8, -4), "the sum function isn't working")

    def test_sub_function_twoZero(self):
        self.assertEqual(0, sub_function(0, 0), "the sum function isn't working")

    def test_sub_function_numZero(self):
        self.assertEqual(5, sub_function(5, 0), "the sum function isn't working")

    def test_sub_function_char(self):
        self.assertEqual(5, sub_function(5, 'f'), "wrong input has been inserted")

# should cover the other funcs
