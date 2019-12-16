# Generate Fibonacci number
# Convert to words

# ---------------------PROGRAM---------------------------------

# Initialize
order = input("Enter order to generate Fibonacci : ")   # Use any order
order = int(order)
f1 = 0
f2 = 1
f_next = 0

# Generate series
for n in range(order):
    if n == 0:
        print(f1)
    else:
        f_next = f1 + f2
        print(f_next)
    f1 = f2     # For next iteration of the loop, f2 is our f1
    f2 = f_next     # For next iteration of the loop, fn is our f2

print("Fibonacci number for order " + str(order) + " is " + str(f_next))

# Convert to words
number_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
number_string = str(f_next)
for x in number_string:
    digit = int(x)              # Convert to number
    word = number_words[digit]
    print(word)                 # Prints word and new line
    # If we need any character at the end of print rather than new line, we can use end=',' as given below
    # print(word, end=" ")  # From list, get corresponding word
