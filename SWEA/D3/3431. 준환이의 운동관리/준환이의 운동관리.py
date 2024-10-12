def result(l, u, x):
    if x < l:
        return l - x
    elif l <= x <= u:
        return 0
    elif x > l:
        return -1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    
    a = result(L, U, X)
    
    print(f"#{test_case} {a}")

