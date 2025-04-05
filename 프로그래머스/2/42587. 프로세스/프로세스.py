from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    order = deque(range(len(priorities)))
    while q:
        for i in range(1, len(q)):
            if len(q) == 1:
                answer += 1
                return answer
            if q[0] < q[i]:
                q.append(q.popleft())
                order.append(order.popleft())
                break
        else:
            answer += 1
            q.popleft()
            temp = order.popleft()
            if temp == location:
                return answer
    return answer