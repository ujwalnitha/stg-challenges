# Get User input, find Fibonacci number of given order and convert to number sentence

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
        fibonacci_number = MyFibonacci.get_fibonacci_number(order)

        # Covert to string
        number_sentence = NumberToWords.get_number_sentence(fibonacci_number)
        print("---------OUTPUT-----------")
        print(str(fibonacci_number) + " - " + str(number_sentence))


if __name__ == '__main__':
    unittest.main()
