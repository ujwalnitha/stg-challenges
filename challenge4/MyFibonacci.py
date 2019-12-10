class MyFibonacci(object):

    def get_fibonacci_number(self, order=1):

        assert order > 0, "Invalid order, must be > 0"

        # Initialize
        f1 = 0
        f2 = 1
        fn = 0

        # Find Fibonacci series number
        for i in range(1, order+1):
            if i == 1:
                fn = f1
            else:
                fn = f1 + f2
            f1 = f2
            f2 = fn
            print(str(i) + " :  " + str(fn))

        print("Fibonacci of order %s is %s" % (order, fn))

        return fn

