def solution(nums):
    answer = 0
    b = []
    for i in range(len(nums)):
        if nums[i] not in b:
            answer += 1
            b.append(nums[i])
        if answer == int(len(nums) / 2):
            break
    return answer