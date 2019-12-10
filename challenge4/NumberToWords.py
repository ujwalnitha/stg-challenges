class NumberToWords(object):

    def get__number_sentence(self, number=1):

        assert number >= 0, "Invalid number, must be > 0"

        number_words = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6:"Six", 7: "Seven", 8: "Eight", 9: "Nine"}

        # Print number words
        temp = number
        number_sentence = ""
        print("---------OUTPUT-----------")
        if number == 0:
            print(str(number) + " - " + str(number_words[0]))
            return
        while temp != 0:
            number_sentence = number_words[temp % 10] + " " + number_sentence
            temp = int(temp/10)
        print(str(number) + " - " + str(number_sentence))
        return

