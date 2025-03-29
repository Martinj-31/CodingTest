import sys

M = int(sys.stdin.readline())

S = []
for i in range(M):
    com = sys.stdin.readline().rstrip().split()
    if com[0] == 'add':
        if com[1] not in S:
            S.append(com[1])
    elif com[0] == 'remove':
        if com[1] in S:
            S.remove(com[1])
    elif com[0] == 'check':
        if com[1] in S:
            print(1)
        else:
            print(0)
    elif com[0] == 'toggle':
        if com[1] in S:
            S.remove(com[1])
        else:
            S.append(com[1])
    elif com[0] == 'all':
        S = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18' ,'19', '20']
    elif com[0] == 'empty':
        S = []