import sys

L = int(sys.stdin.readline())
temp = sys.stdin.readline().rstrip()
string = []
for i in range(L):
    string.append(temp[i])

critetion = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for i, s in enumerate(critetion):
    dic[s] = i + 1

result = 0
for i, s in enumerate(string):
    result += dic[s] * 31**i

print(result)