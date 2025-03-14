import sys

s = 0
ss = 0
for i in range(20):
    info = list(sys.stdin.readline().split())
    name, credit, score = info[0], float(info[1]), info[2]

    m = 0
    if score == "A+":
        m = 4.5
    elif score == "A0":
        m = 4.0
    elif score == "B+":
        m = 3.5
    elif score == "B0":
        m = 3.0
    elif score == "C+":
        m = 2.5
    elif score == "C0":
        m = 2.0
    elif score == "D+":
        m = 1.5
    elif score == "D0":
        m = 1.0
    elif score == "F":
        m = 0.0
    elif score == "P":
        continue
    s += m * credit
    ss += credit

print(s / ss)