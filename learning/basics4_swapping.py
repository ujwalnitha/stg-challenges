'''
Block Comment - Add 3 single quotes
Starts and ends with three quotes

References:
Simple programs: https://www.programiz.com/python-programming/examples

This simple code is to swap values using a temporary variable

'''

# Suppose if we have water in two containers, how will we swap.
# We have to use another container to save and free up one container
# Likewise, if we have to use a temporary variable

# ---------------------PROGRAM---------------------------------

# Initialize variables
x = 5
y = 6
print("Before swapping")
print("First number " + str(x))
print("Second number " + str(y))

# Swap and Print
temp = x    # temp becomes 5
x = y       # x becomes 6
y = temp    # y becomes 5
print("After swapping")
print("First number " + str(x))
print("Second number " + str(y))
