import sys

T = int(sys.stdin.readline())


for t in range(T):
    N = int(sys.stdin.readline())

    dp = [0] * 100
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2
    if N >= 5:
        for i in range(5, N):
            dp[i] = dp[i - 1] + dp[i - 5]
    print(dp[N - 1])
