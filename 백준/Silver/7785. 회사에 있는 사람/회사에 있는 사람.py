import sys

n = int(sys.stdin.readline())

office = {}
for i in range(n):
    name, status = sys.stdin.readline().rstrip().split()
    if status == 'enter':
        office[name] = 1
    if status == 'leave':
        office[name] = 0
office_name = sorted(office.keys(), reverse=True)

for i in office_name:
    if office[i] == 1:
        print(i)