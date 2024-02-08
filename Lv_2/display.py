import sys

T = int(sys.stdin.readline())
seven_segment = {}
seven_segment['10'] = [0, 0, 0, 0, 0, 0, 0]
seven_segment['0'] = [1, 1, 1, 1, 1, 1, 0]
seven_segment['1'] = [0, 1, 1, 0, 0, 0, 0]
seven_segment['2'] = [1, 1, 0, 1, 1, 0, 1]
seven_segment['3'] = [1, 1, 1, 1, 0, 0, 1]
seven_segment['4'] = [0, 1, 1, 0, 0, 1, 1]
seven_segment['5'] = [1, 0, 1, 1, 0, 1, 1]
seven_segment['6'] = [1, 0, 1, 1, 1, 1, 1]
seven_segment['7'] = [1, 1, 1, 0, 0, 1, 0]
seven_segment['8'] = [1, 1, 1, 1, 1, 1, 1]
seven_segment['9'] = [1, 1, 1, 1, 0, 1, 1]

for _ in range(T):
    num1, num2 = sys.stdin.readline().split()
    num1_list = list(num1)
    num2_list = list(num2)

    t1 = 5 - len(num1_list)
    t2 = 5 - len(num2_list)
    for _ in range(t1):
        num1_list.insert(0, '10')
    for _ in range(t2):
        num2_list.insert(0, '10')
        
    cnt = 0
    for i in range(5):
        a = seven_segment[num1_list[-i-1]]
        b = seven_segment[num2_list[-i-1]]
        for j in range(7):
            if a[j] != b[j]:
                cnt += 1
            else: pass
    print(cnt)
    