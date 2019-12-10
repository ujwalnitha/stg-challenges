class NumberToWords(object):

    @staticmethod
    def get_number_sentence(number=1):

        assert number >= 0, "Invalid number, must be > 0"

        number_words = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6:"Six", 7: "Seven", 8: "Eight", 9: "Nine"}

        # Print number words
        number_sentence = ""

        if number == 0:
            return number_words[0]

        while number != 0:
            number_sentence = number_words[number % 10] + " " + number_sentence
            number = int(number/10)

        return number_sentence

