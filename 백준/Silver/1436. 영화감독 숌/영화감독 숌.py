import sys

n = int(sys.stdin.readline())

cnt = 600
ver = 0
while True:
    cnt += 1
    N = str(cnt)
    for i in range(len(N)-2):
        if N[-i-1] == '6' and N[-i-2] == '6' and N[-i-3] == '6':
            ver += 1
            break
    if ver == n:
        break

print(cnt)