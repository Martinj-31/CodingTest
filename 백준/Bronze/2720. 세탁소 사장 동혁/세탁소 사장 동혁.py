import sys

T = int(sys.stdin.readline())

for t in range(T):
    C = int(sys.stdin.readline())

    q = C // 25
    q_re = C % 25

    C -= 25*q

    d = C // 10
    d_re = C % 10

    C -= 10*d

    n = C // 5
    n_re = C % 5

    C -= 5*n

    p = C // 1
    p_re = C % 1

    print(q, d, n, p)