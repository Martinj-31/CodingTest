import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


def prefix_sum(n):
    li = [0] * n
    li[0] = nums[0]
    for i in range(1, n):
        li[i] = nums[i] + li[i - 1]
    return li


p_sum = prefix_sum(N)

for m in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:
        print(p_sum[end - 1])
    else:
        print(p_sum[end - 1] - p_sum[start - 2])