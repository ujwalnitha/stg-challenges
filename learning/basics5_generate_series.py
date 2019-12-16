'''
Generate a series without loop
Print 5 numbers in the series
Each number will be x-y

References:
https://www.programiz.com/python-programming/operators

'''

# ---------------------PROGRAM---------------------------------

# Initialize variables
x = 40
y = 10

# First number
next_number = x - y
print(next_number)

# Second number
next_number = next_number - y
print(next_number)

# Third number
next_number = next_number - y
print(next_number)

# Forth number
next_number = next_number - y
print(next_number)

# Fifth number
next_number = next_number - y
print(next_number)

# x = x + y can be also written as x += y and x = x - y as x -= y etc, it is a combination of (operator+assignment)
