import sys

N, K = map(int, sys.stdin.readline().split())


def tracker(arr, start):
    if len(arr) == K:
        print(*arr)
        return

    for idx in range(start, N + 1):
        arr.append(idx)
        tracker(arr, idx)
        idx += 1
        arr.pop()


li = [i for i in range(1, N + 1)]

tracker([], 1)