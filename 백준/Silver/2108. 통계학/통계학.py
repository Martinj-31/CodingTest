import sys
from collections import Counter

N = int(sys.stdin.readline())

li = [int(sys.stdin.readline()) for _ in range(N)]
li.sort()
print(round(sum(li) / N))
print(li[(N - 1) // 2])
cnt = Counter(li).most_common(2)
if len(li) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(li[-1] - li[0])