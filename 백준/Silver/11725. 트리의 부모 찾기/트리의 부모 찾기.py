import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(node):
    for i in tree[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)


visited = [0] * (N + 1)
dfs(1)

for i in range(2, N + 1):
    print(visited[i])