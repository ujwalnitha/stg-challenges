'''
Generate Fibonacci series and number of given order

Fibonacci series is 0,1,1,2,3,5,8,13,21 etc
Formula is like following
f1 = 0
f2 = 1
fnext = f1 + f2

If the order is 5, we have to apply formula 3 times
Series : 0,1,1,2,3,5
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
'''

# ---------------------PROGRAM---------------------------------

# Initialize
order = 5   # Use any order
f1 = 0
f2 = 1
fn = 0

# Generate series
for n in range(order):
    if n == 0:
        print(f1)
    else:
        fn = f1 + f2
        print(fn)
    f1 = f2     # For next iteration of the loop, f2 is our f1
    f2 = fn     # For next iteration of the loop, fn is our f2

print("Fibonacci number for order " + str(order) + " is " + str(fn))