'''
Block Comment - Add 3 single quotes
Starts and ends with three quotes

References:
https://www.w3schools.com/python/ref_func_print.asp
https://www.tutorialspoint.com/python/python_strings.htm
https://pyformat.info/

This simple code is to check how to print in different ways

'''

# Print method prints to output console
# Whatever is given inside print() should not break any rules of type conversion
# print(number) and print("string") will work, but if we give print(number + "string") will not work
# so we have to use type conversions to avoid error

# ---------------------PROGRAM---------------------------------

# Initialize variables, print type
age = 17            # number, type int
name = "Anonymous"  # string, type str

print(age)
print(name)

# print(age + name) # This throws Error "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
print(str(age) + name)  # This will work as string concatenation, because "17" + "Anonymous" is allowed.

# print using + concatenation
print("I am " + str(age) + " years old, and my name is " + name + ". Thank you!")   # Format the we want
print("I am %s years old, and my name is %s. Thank you!" % (str(age), name))    # Prints same, but we are providing variables at the end