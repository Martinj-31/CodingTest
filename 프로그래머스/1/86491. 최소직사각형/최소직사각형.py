def solution(sizes):
    answer = 0
    width = []
    height = []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            width.append(sizes[i][1])
            height.append(sizes[i][0])
        else:
            width.append(sizes[i][0])
            height.append(sizes[i][1])
    max_width = max(width)
    max_height = max(height)
    answer = max_width * max_height
    
    return answer