import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

or_li = sorted(list(set(li)))
dic = {or_li[i] : i for i in range(len(or_li))}

for i in li:
    print(dic[i], end=" ")
