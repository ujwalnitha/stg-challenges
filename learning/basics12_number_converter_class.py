''''

This file is to wrap number to words code in a class

Reference: https://www.w3schools.com/python/python_classes.asp

If we have to use a method from Class, outside calling file
-we have to import the class in calling file
-create an object and call function
-if it is a static function, call ClassName.function_name()

This method will just digits to words, not to a number sentence wrt to digit place

'''


class NumberToWordsClass:

    def get_number_in_word(self, input_number=0):
        number_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        # Each item in list hs index starting from 0, so number_words[2] will return "Two" in this case

        # using conversion to string to tokenize
        number_string = str(input_number)
        number_sentence = ""
        for x in number_string:
            digit = int(x)  # Convert to number
            word = number_words[digit]
            print(word)  # From list, get corresponding word
            number_sentence = number_sentence + number_words[digit] + " "

        return number_sentence
