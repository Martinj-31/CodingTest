str = input()

for letter in str:
    if letter.isupper():
        print(letter.lower(), end="")
    else:
        print(letter.upper(), end="")