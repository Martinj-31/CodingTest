import sys

K, N = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(K)]

lt, rt = 1, max(li)
while lt <= rt:
    mid = (lt + rt) // 2
    num = 0
    for i in li:
        num += i // mid
    if N <= num:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)