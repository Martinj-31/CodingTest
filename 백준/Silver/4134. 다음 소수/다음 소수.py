import sys, math

T = int(sys.stdin.readline())

for t in range(T):
    num = int(sys.stdin.readline())

    while True:
        if num == 1 or num == 0:
            num += 1
            continue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            print(num)
            break
        num += 1
