def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a,b)

a, b = 2023, 4913
print('The GCD of %d and %d is %d' % (a, b, gcd(a, b)))
print('The LCM of %d and %d is %d' % (a, b, lcm(a, b)))
