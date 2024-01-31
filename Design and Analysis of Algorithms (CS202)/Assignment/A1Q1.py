import sys

def power_modulo(m, k, n):
    if k == 0:
        return 1    
    if k % 2 == 0:
        return (power_modulo(m, k/2, n) * power_modulo(m, k/2, n)) % n
    else:
        return ((m % n) * power_modulo(m, (k-1)/2, n) * power_modulo(m, (k-1)/2, n)) % n

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))
