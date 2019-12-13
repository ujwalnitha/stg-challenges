from challenge4.NumberToWords import *

myList = []
for i in range(999999,1000011):
    myList.append(NumberToWords.get_number_sentence(i))

for i in myList:
    print(i)