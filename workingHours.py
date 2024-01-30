import sys

HH = 0
MM = 0
for i in range(5):
    time = list(sys.stdin.readline().split())
    start_hh, start_mm = map(int, time[0].split(':'))
    end_hh, end_mm = map(int, time[1].split(':'))
    HH += (end_hh-start_hh)*60
    MM += (end_mm-start_mm)
print(HH+MM)