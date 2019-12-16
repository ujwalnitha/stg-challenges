'''

List to store all number words
https://www.w3schools.com/python/python_lists.asp

Tokenize number and find corresponding word from list
'''

number_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
# Each item in list hs index starting from 0, so number_words[2] will return "Two" in this case

input_number = 208
# using conversion to string to tokenize
number_string = str(input_number)
for x in number_string:
    digit = int(x)              # Convert to number
    print(number_words[digit])  # From list, get corresponding word
