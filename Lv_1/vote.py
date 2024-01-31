import sys

T = int(sys.stdin.readline())

for _ in range(T):
    bundle_p = ''
    each_p = ''
    n = int(sys.stdin.readline())
    a = n // 5
    b = n % 5
    bundle = '++++'
    each = '|'
    for i in range(a):
        if i == a-1:
            bundle_p += bundle
        else: bundle_p += bundle + ' '
    for j in range(b):
        each_p += each
    if a != 0 and b != 0:
        each_p = ' ' + each_p
    else: pass
    print(bundle_p + each_p)