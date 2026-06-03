import time

def char_to_ascii(char):
    ascii_code = ord(char)
    return (f"The ASCII code for '{char}' is: {ascii_code}")

def ascii_to_char(ascii_code):
    character = chr(ascii_code)
    return (f"The character for ASCII code '{ascii_code}' is: {character}")

while True:

    print("==============================")
    print("- Character to ASCII (1)      ")
    print("- ASCII to Character (2)      ")
    print("==============================")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        char = input("Enter a character: ")
        print(char_to_ascii(char))
    elif choice == '2':
        ascii_code = int(input("Enter an ASCII code (0-127): "))
        print(ascii_to_char(ascii_code))
    else:
        print("Invalid choice. Please enter 1 or 2.")
    
    time.sleep(2)