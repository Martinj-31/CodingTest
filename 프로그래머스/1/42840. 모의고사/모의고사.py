def solution(answers):
    answer = []
    man1, man2, man3 = 0, 0, 0
    man1_rule = [1, 2, 3, 4, 5]
    man2_rule = [2, 1, 2, 3, 2, 4, 2, 5]
    man3_rule = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == man1_rule[i%len(man1_rule)]:
            man1 += 1
        if answers[i] == man2_rule[i%len(man2_rule)]:
            man2 += 1
        if answers[i] == man3_rule[i%len(man3_rule)]:
            man3 += 1
    arr = [man1, man2, man3]
    max_num = max(arr)
    for i in range(len(arr)):
        if max_num <= arr[i]:
            max_num = arr[i]
            answer.append(i + 1)
    return answer