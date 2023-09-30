def main():
    # Prompt the user to input the text.
    text = input("Enter text: ")
    # Prompt the user to input the shift value.
    shift = int(input("Enter shift: "))

    # Encrypt the text using the Caesar cipher with the specified shift and print the result.
    print(encrypt(text, shift))


def encrypt(input_text, shift):
    encrypted_text = ""
    for char in input_text:
        if char.isalpha():
            # Convert the character to its ASCII code.
            char_code = ord(char)
            # Apply the Caesar cipher shift.
            char_code += shift
            # Ensure the result remains within the alphabet range.
            if char.islower() and char_code > ord("z"):
                char_code -= 26
            elif char.isupper() and char_code > ord("Z"):
                char_code -= 26
            # Convert the ASCII code back to a character.
            encrypted_char = chr(char_code)
            encrypted_text += encrypted_char
        else:
            # If the character is not a letter, keep it unchanged.
            encrypted_text += char

    return encrypted_text


if __name__ == "__main__":
    main()
