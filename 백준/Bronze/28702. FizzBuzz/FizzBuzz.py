import sys

a = 0
for i in range(3):
    num = sys.stdin.readline().rstrip()
    if num == "Fizz" or num == "Buzz" or num == "FizzBuzz":
        if a != 0:
            a += 1
    else:
        a = int(num)

a += 1

if a % 5 == 0 and a % 3 == 0:
    print("FizzBuzz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0:
    print("Fizz")
else:
    print(a)