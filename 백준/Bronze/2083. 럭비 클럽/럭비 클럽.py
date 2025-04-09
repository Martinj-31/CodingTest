import sys

while True:
    name, age, weight = list(sys.stdin.readline().rstrip().split())
    if name == "#":
        break
    if int(age) > 17 or int(weight) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")
