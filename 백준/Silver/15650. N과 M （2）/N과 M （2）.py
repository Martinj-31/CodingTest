import sys

N, K = map(int, sys.stdin.readline().split())


def tracker(arr, now_length, visited):
    if now_length == K:
        flag = True
        for a in range(1, len(arr)):
            if arr[a - 1] > arr[a]:
                flag = False
                break
        if flag:
            print(*arr)
        return

    for idx in range(1, N + 1):
        if not visited[idx]:
            arr.append(idx)
            visited[idx] = True
            tracker(arr, now_length + 1, visited)
            arr.pop()
            visited[idx] = False


result = []
li = [i for i in range(1, N + 1)]
visited = [False] * (N + 1)

tracker([], 0, visited)