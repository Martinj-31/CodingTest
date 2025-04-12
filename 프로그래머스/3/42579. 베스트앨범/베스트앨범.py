def solution(genres, plays):
    ans = []
    n = len(genres)
    Genre = {}
    
    total = [[genres[i],plays[i],i] for i in range(n)]
    total = sorted(total, key=lambda x : (x[0], -x[1], x[2]))
    
    for i in total :
        if i[0] not in Genre:
            Genre[i[0]] = i[1]
        else :
            Genre[i[0]] += i[1]
    
    Genre = sorted(Genre.items(), key=lambda x : -x[1])
    
    for i in range(len(Genre)):
        tmp = 0
        for j in range(n):
            if (Genre[i][0] == total[j][0]) and (tmp < 2) :
                ans.append(total[j][2])
                tmp += 1

    return ans