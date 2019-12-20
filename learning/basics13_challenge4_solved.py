# Get User input, find Fibonacci number of given order and convert to number sentence

import unittest

# import all(*) from our helper modules
from learning.basics11_fibonacci_class import *
from learning.basics12_number_converter_class import *


class Challenge4_solved(unittest.TestCase):

    def test_challenge4(self):

        # Get order
        order = input("Enter Fibonacci series order(integer) : ")
        order = int(order)
        assert order > 0, "Invalid order"

        # Get Fibonacci number
        # get_fibonacci_number() is a static method, so ClassName.method_name() can be used
        fibonacci_number = MyFibonacciClass.get_fibonacci_number(order)

        # Covert to string
        # get_number_in_word() is not a static method, so we have to create object of the class in order to call the method
        number_words_object = NumberToWordsClass()
        number_sentence = number_words_object.get_number_in_word(fibonacci_number)
        print("---------OUTPUT-----------")
        print(str(fibonacci_number) + " - " + str(number_sentence))


if __name__ == '__main__':
    unittest.main()
