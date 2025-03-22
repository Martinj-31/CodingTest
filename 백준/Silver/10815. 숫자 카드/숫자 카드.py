import sys

N = int(sys.stdin.readline())
Ns = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
Ms = list(map(int, sys.stdin.readline().split()))

Ns.sort()
for num in Ms:
    l_idx, r_idx = 0, N - 1
    isExist = False

    while l_idx <= r_idx:
        mid = (l_idx + r_idx) // 2
        if Ns[mid] == num:
            print(1, end=" ")
            isExist = True
            break
        elif Ns[mid] < num:
            l_idx = mid + 1
        else:
            r_idx = mid - 1

    if not isExist:
        print(0, end=" ")