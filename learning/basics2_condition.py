'''
Block Comment - Add 3 single quotes
Starts and ends with three quotes

References:
https://www.w3schools.com/python/python_conditions.asp
https://www.w3schools.com/python/ref_func_type.asp

This simple code is to find if a number is greater than or less than or equal to 0

'''

# Read user input, assign to a variable
# use if - else to find the type of number
# 'input' is a built in function to read user input, press (ctrl + click) to read more about it

# ---------------------PROGRAM---------------------------------

# Initialize variables, print type
user_input = input("Enter Fibonacci series order(integer) : ")
print(type(user_input))

# Convert input to number, because input() reads input as a string
input_number = int(user_input)
print(type(input_number))

# check if the number equal to 0
if input_number == 0:
    print("Number is 0")
else:
    if input_number > 0:
        print("Number is greater than 0")
    elif input_number < 0:
        print("Number is less than 0")

# elif is actually else+if, used when else has a condition to check
# in this case we can use just else:, because a number if not equal to 0 and not >0, will be <0