import sys

N = int(sys.stdin.readline())

result = 1
for i in range(1, N + 1):
    result *= i

str_n = str(result)

cnt = 0
for i in range(len(str_n) - 1, 0, -1):
    if int(str_n[i]) == 0:
        cnt += 1
    if int(str_n[i]) > 0:
        break

print(cnt)