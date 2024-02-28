import sys

def LCMS(a, b):
    return int(len(a) / 14 + len(b) / 8)

num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = [int(s) for s in sys.stdin.readline().split()]
    b = [int(s) for s in sys.stdin.readline().split()]
    print(LCMS(a, b))
