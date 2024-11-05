def solution(brown, yellow):
    answer = []
    width = 0
    height = 0
    for i in range(yellow):
        if yellow % (i + 1) != 0:
            continue
        w, h = (i + 1) + 2, (yellow / (i + 1)) + 2
        print(w, h)
        if 2 * w + 2 * h - 4 == brown:
            answer = [int(h), int(w)]
            break
    print(answer)
    return answer