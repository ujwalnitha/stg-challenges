''''

This file is to wrap fibonacci code in a class

Reference: https://www.w3schools.com/python/python_classes.asp

If we have to use a method from Class, outside calling file
-we have to import the class in calling file
-create an object and call function
-if it is a static function, call ClassName.function_name()

'''


class MyFibonacciClass:

    @staticmethod
    def get_fibonacci_number(order=1):
        # Initialize
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
            f1 = f2  # For next iteration of the loop, f2 is our f1
            f2 = fn  # For next iteration of the loop, fn is our f2

        print("Fibonacci number for order " + str(order) + " is " + str(fn))
        return fn
