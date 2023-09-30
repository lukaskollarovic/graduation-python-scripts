def main():
    # Prompt the user to input a sentence
    sentence = input("Enter a sentence: ")

    # Initialize counters for words, characters, digits, and spaces
    words = 1  # We start at 1 because we distinguish words by spaces, and the first word doesn't have a space before it
    characters = 0
    digits = 0
    spaces = 0

    # Iterate through each character in the sentence
    for char in sentence:
        if char == " ":
            words += 1  # Count spaces to determine the number of words
            spaces += 1
        elif char.isdigit():
            digits += 1  # Count digits
            characters += 1  # Count characters (including digits)
        elif char.isalpha():
            characters += 1  # Count characters (excluding digits)

    # Print the analysis results
    print("The text contains:")
    print(f"{words} words")
    print(f"{characters} characters")
    print(f"{digits} digits")
    print(f"{spaces} spaces")


if __name__ == "__main__":
    main()
