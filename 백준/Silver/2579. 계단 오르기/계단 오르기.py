import sys

N = int(sys.stdin.readline())
step = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0] * N

if len(step) <= 2:
    print(sum(step))
else:
    dp[0] = step[0]
    dp[1] = step[0] + step[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])
    print(dp[-1])