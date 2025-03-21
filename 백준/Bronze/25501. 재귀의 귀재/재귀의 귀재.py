import sys

N = int(sys.stdin.readline())


def recursion(text, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif text[l] != text[r]:
        return 0, cnt
    else:
        return recursion(text, l+1, r-1, cnt + 1)


def isPalindrome(text):
    return recursion(text, 0, len(text) - 1, 1)


for _ in range(N):
    result = isPalindrome(sys.stdin.readline().rstrip())
    print(result[0], result[1])