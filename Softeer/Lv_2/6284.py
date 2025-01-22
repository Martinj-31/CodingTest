def calculate_virus_count(K, P, N):
    MOD = 1000000007
    result = K
    for _ in range(N):
        result = (result * P) % MOD
    return result

K, P, N = map(int, input().split())

result = calculate_virus_count(K, P, N)
print(result)