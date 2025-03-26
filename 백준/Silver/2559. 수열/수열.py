import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


temp_sum = sum(nums[:M])
result = temp_sum

for i in range(N - M):
    temp_sum += nums[i + M] - nums[i]
    if result < temp_sum:
        result = temp_sum

print(result)