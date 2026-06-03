# ASCII Converter Snippet
character = input("Enter a single letter: ")
ascii_code = ord(character)
print("The ASCII code is:", ascii_code)

next_code = ascii_code + 1
next_character = chr(next_code)
print("The next letter in the alphabet is:", next_character)