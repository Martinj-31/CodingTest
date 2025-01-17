import sys

M, N, K = map(int, sys.stdin.readline().split())

secret = list(map(int, sys.stdin.readline().split()))

buttons = list(map(int, sys.stdin.readline().split()))

flag = False
if len(buttons) < len(secret):
    print(f"normal")
elif len(buttons) == len(secret):
    if buttons == secret:
        print(f"secret")
    else:
        print(f"normal")
else:
    for i in range(len(buttons)-len(secret)+1):
        if buttons[i:i+len(secret)] == secret:
            flag = True
        else: pass
    if flag == True:
        print(f"secret")
    else:
        print(f"normal")