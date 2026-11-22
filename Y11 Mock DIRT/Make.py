letter = ""

while letter.upper() != "X":
    if letter != "Z":
        letter = input()
        print(chr(ord(letter.upper()) + 1))
    else:
        letter = input()
        print("A")
