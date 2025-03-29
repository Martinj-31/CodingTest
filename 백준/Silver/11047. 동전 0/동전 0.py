import sys

N, K = map(int, sys.stdin.readline().split())

money = []
cnt = 0
for i in range(N):
    money.append(int(sys.stdin.readline()))
money.sort(reverse=True)
for i in money:
    if i <= K:
        cnt += K // i
        K = K % i
print(cnt)