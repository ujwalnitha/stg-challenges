'''
Number to string and getting characters one by one

Remainder vs division operator

https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/

'''

print(".....................................")
# Easiest way to tokenize a number to digits is convert to a string and do loop
# for loop on a string gives letters one by one
# if required we can covert it back to number by using int()
number = 200
number_string = str(number)
for x in number_string:
    print(x)


# Modulo operator % gives the remainder of division
# / operator gives quotient, decimal
# if we need integer part, do type conversion like int(5/2)
# ---------------------PROGRAM---------------------------------


print(5/2)          # 2.5
print(int(5/2))     # 2
print(5 % 2)        # 1 , remainder


# Another way to tokenize a number is to use remainder and division
# 155 - to 1,5,5
# 155 % 10 -> 5
# then do int (155 / 10) -> 15
# repeat same until number is 0

print(".........Tokens............")
# Initialize
number = 155
# while is another type of loop, usage while condition:
# repeats until condition is satisfied
while number != 0:
    print(number % 10)
    number = int(number/10)
