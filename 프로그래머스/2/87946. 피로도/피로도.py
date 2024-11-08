answer = -1
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = 0

def solution(k, dungeons):
    global visited
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons)

    return answer
