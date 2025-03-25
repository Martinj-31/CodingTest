import sys

count = 1
temp = True
stack = []
op = []

N = int(sys.stdin.readline())
for i in range(N):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)
