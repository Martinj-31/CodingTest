import sys

N = int(sys.stdin.readline())

for i in range(1, 2*N):
    if i == N:
        print("*"*(2*N - 1))
    elif i < N:
        print(" "*(N - i - 1), "*"*(2*i - 1))
    elif i > N:
        print(" "*(i - N - 1), "*"*(2*N - 2*(i - N) - 1))