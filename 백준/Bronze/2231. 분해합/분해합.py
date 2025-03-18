import sys

N = int(sys.stdin.readline())

li = []
for i in range(1, N):
    num = str(i)
    re = i
    for j in range(len(num)):
        re += int(num[j])
    if re == N:
        li.append(i)

if len(li) == 0:
    print(0)
else:
    print(li[0])