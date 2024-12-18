def solution(s):
    answer = True
    hist = []
    for i in range(len(s)):
        if s[i] == "(":
            hist.append(s[i])
        elif s[i] == ")":
            if len(hist) > 0:
                hist.pop()
            else:
                answer = False
    if len(hist) > 0:
        answer = False

    return answer