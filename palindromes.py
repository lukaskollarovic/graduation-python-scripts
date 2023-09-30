def main():
    # Prompt the user to enter a text.
    text = input("Enter text: ")

    # Call the 'check_palindrom' function to find palindromes in the text.
    palindromes = check_palindromes(text)

    # Print the detected palindromes.
    print("Palindromes: " + ", ".join(palindromes))


def check_palindromes(text):
    # Split the input text into words.
    words = text.split()

    # Initialize an empty list to store palindromes.
    palindromes = []

    # Iterate through each word in the text.
    for word in words:
        # Check if the word is the same when reversed.
        if word == word[::-1]:
            # If it is, add it to the list of palindromes.
            palindromes.append(word)

    return palindromes


if __name__ == "__main__":
    main()
