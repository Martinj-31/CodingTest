from collections import deque
import sys

# 층 수, 상호, 스타트링크, 업 버튼, 다운 버튼
F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [0] * (F + 1)

def bfs():
    q = deque()
    q.append(S)
    visited[S] = 1
    while q:
        x = q.popleft()
        if x == G:
            return visited[x]-1
        else:
            for j in (x + U, x - D):
                if 0 < j <= F and not visited[j]:
                    visited[j] = visited[x] + 1
                    q.append(j)
    return "use the stairs"
print(bfs())