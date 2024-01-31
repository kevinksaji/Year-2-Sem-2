def factorial(n):
    if n == 1: # base case
        return 1
    else:
        return n * factorial(n-1)

def factorial_verbose(n, indent):
    print(' ' * (2 * indent) + "executing factorial of " + str(n))
    if n == 1:
        print(' ' * (2 * indent) + "returning factorial of " + str(n))
        return 1
    else:
        print(' ' * (2 * indent) + "calling factorial of " + str(n-1))
        fv = factorial_verbose(n-1, indent+1)
        print(' ' * (2 * indent) + "returning factorial of " + str(n))
        return n * fv

factorial_verbose(5, 0)
