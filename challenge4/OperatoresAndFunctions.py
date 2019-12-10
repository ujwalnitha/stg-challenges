
import unittest

from challenge4.MyFibonacci import *
from challenge4.NumberToWords import *


class Challenge4(unittest.TestCase):

    def test_operators_functions(self):

        # Get order
        order = input("Enter Fibonacci series order(integer) : ")
        try:
            order = int(order)
        except ValueError:
            assert False, "Invalid input, please enter a number > 0"

        # Get Fibonacci number
        fib_obj = MyFibonacci()
        fibonacci_number = fib_obj.get_fibonacci_number(order)

        # Covert to string
        number_to_string_obj = NumberToWords()
        number_to_string_obj.get__number_sentence(fibonacci_number)


if __name__ == '__main__':
    unittest.main()
