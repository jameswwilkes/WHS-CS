def encrypt_character(plain_char, shift_value):
    plain_char_code = ord(plain_char)
    shifted_char_code = plain_char_code + shift_value
    
    if shifted_char_code > 90:
        shifted_char_code -= 26

    return chr(shifted_char_code)

plain_char = input("Enter a character to shift: ")
shift_value = int(input("Enter the shift value (integer): "))
encrypted_char = encrypt_character(plain_char, shift_value)
print(f"The encrypted character is: {encrypted_char}")