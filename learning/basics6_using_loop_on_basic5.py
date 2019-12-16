'''
Included simple loop examples too
Generate a series with loop
Print 5 numbers in the series
Each number will be x-y

References:
https://www.w3schools.com/python/python_for_loops.asp

'''

# ---------------------PROGRAM---------------------------------

# Simple loop to print, range() is an in- build function, do ctrl+click for more details
# Prints 0 - 4
print("-----------------")
for x in range(5):
    print(x)

print("-----------------")
# Prints 1 - 5
for x in range(1, 6):
    print(x)

# Breaking from loop, break stops the loop and exits from loop and control goes to line after loop
# Prints 1,2
print("-----------------")
for x in range(1, 6):
    if x == 3:
        print("Stopping loop")
        break
    print(x)

print("-----------------")
# Continuing loop skipping following lines in the loop
# Prints 1,2,Skipping print for 3, 4,5
for x in range(1, 6):
    if x == 3:
        print("Skipping print for 3")
        continue
    print(x)

print("-------Series----------")
# Initialize variables
x = 40
y = 10

# Initialize variable for the loop
next_number = x - y
for i in range(5):
    print(next_number)
    next_number = next_number - y