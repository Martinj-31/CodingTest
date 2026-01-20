def solution(my_string, overwrite_string, s):
    answer = ''
    for idx, l in enumerate(my_string):
        if s <= idx <= s + len(overwrite_string) - 1:
            answer += overwrite_string[idx - s]
        else:
            answer += l
    return answer