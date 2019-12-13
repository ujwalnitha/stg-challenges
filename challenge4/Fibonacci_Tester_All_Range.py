from challenge4.NumberToWords import *
from challenge4.MyFibonacci import *

myList = {}
for i in range(1,35):
    fib_num = MyFibonacci.get_fibonacci_number(i)
    myList[fib_num] = (NumberToWords.get_number_sentence(fib_num))

for key, value in myList.items():
    print(str(key) + "-" + str(value))