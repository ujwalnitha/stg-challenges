class NumberToWords(object):

    @staticmethod
    def get_number_sentence(number=1):

        assert number >= 0, "Invalid number, must be > 0"

        if number >= 1000000:
            return ">= Million "

        unit_place_number_words = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        tenth_place_number_words = {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}
        tens_number_words = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty",7: "Seventy", 8: "Eighty", 9: "Ninety"}
        higher_number_words = {2: "Hundred", 3: "Thousand"}

        if number == 0:
            return unit_place_number_words[0]

        # Tokenize
        tokens = []
        temp = number
        while temp != 0:
            tokens.append(temp % 10)
            temp = int(temp/10)
        print("Tokenize : " + str(tokens))

        size = len(tokens)
        print("Number of places : " + str(size))

        number_sentence = " "
        thousand_found = False
        for position in range(size):

            digit = tokens[position]
            if digit == 0:
                continue
            if position == 0:
                number_sentence = unit_place_number_words[digit]

            if position == 1:
                if digit == 1:
                    number_sentence = tenth_place_number_words[tokens[0]]
                else:
                    number_sentence = tens_number_words[digit] + " " + number_sentence

            if position == 2:
                number_sentence = unit_place_number_words[digit] + " " + higher_number_words[position] + " " + number_sentence

            if not thousand_found and 2 < position < 6:
                thousand_found = True
                number_sentence = NumberToWords.get_number_sentence(int(number/1000)) + " " + higher_number_words[3] + " " + number_sentence

        return number_sentence

