import sys

sen = sys.stdin.readline().rstrip()

result = set()
for i in range(len(sen)):
    for j in range(i, len(sen)):
        result.add(sen[i:j + 1])

print(len(result))