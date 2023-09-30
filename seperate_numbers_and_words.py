def main():
    # Get input text from the user and split it into words.
    text = input("Enter text: ").split(" ")

    # Initialize empty strings to store numbers and words separately.
    numbers = ""
    words = ""

    # Iterate through each word in the text.
    for x in text:
        if x.isdigit():  # Check if the word is a digit (number).
            numbers += str(x) + " "  # Append the number to the numbers string.
        else:
            words += (
                x + ","
            )  # Append the word to the words string, separated by a comma.

    # Print the numbers and words found in the text.
    print(f"Numbers in the text are: {numbers}")
    print(f"Words in the text are: {words}")


if __name__ == "__main__":
    main()
