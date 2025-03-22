import sys

N, K = map(int, sys.stdin.readline().split())


def tracker(arr, now_length):
    if now_length == K:
        print(*arr)
        return

    for idx in range(1, N + 1):
        arr.append(idx)
        tracker(arr, now_length + 1)
        arr.pop()


result = []
li = [i for i in range(1, N + 1)]

tracker([], 0)