import sys

def power_modulo(m, k, n):
    if k == 0:
        return 1    
    if k % 2 == 0:
        temp1 = power_modulo(m, k/2, n)
        return (temp1 * temp1) % n
    else:
        temp2 = power_modulo(m, (k-1)/2, n)
        return ((m % n) * temp2 * temp2) % n

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))
