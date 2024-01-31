def fibonacci(n):
    if n == 1 or n == 2: # base case
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# Note how long the following takes
print(fibonacci(100))