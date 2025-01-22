import sys

N = int(sys.stdin.readline())

temp = []
for i in range(N):
    numstr = sys.stdin.readline()
    if '.' in numstr:
        inte, deci = numstr.split('.')
        deci = deci.rstrip()
    else:
        inte, deci = numstr, -1
    temp.append([int(inte), int(deci)])
    temp.sort(key = lambda x: (x[0], x[1]))

for i in range(N):
    if temp[i][1] == -1:
        print(str(temp[i][0]))
    else:
        print(str(temp[i][0]) + '.' + str(temp[i][1]))