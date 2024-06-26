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
