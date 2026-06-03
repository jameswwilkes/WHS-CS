# ASCII Converter Snippet
character = int(input("Enter an integer 1-128: "))
ascii_code = chr(character)
print("The ASCII code is:", ascii_code)

next_code = character - 1
next_character = chr(next_code)
print("The previous letter in the alphabet is:", next_character)