import sys

mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    sentence = list(sys.stdin.readline().rstrip())
    if sentence == ["#"]:
        break
    cnt = 0
    for s in sentence:
        if s in mo:
            cnt += 1
    print(cnt)
