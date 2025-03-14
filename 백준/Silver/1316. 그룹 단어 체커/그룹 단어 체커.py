import sys

N = int(sys.stdin.readline())

r = 0
for i in range(N):
    bin = []
    word = list(sys.stdin.readline().rstrip())
    flag = True

    bin.append(word[0])
    for i, w in enumerate(word):
        if i == 0:
            continue
        else:
            if w in bin:
                if w == bin[-1]:
                    continue
                else:
                    flag = False
                    break
        bin.append(w)
    if flag:
        r += 1

print(r)