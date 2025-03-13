import sys

N = int(sys.stdin.readline())
A = int(sys.stdin.readline())
result = 0

for i in range(N):
    result += (A % 10**(i+1)) // 10**(i)
    A -= A % 10**(i+1)
print(result)