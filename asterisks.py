def main():
    # Prompt the user to enter a sentence
    sentence = input("Enter a sentence: ")

    # Prompt the user to enter a word to be masked (starred out)
    word_to_mask = input("Enter the word you want to mask with asterisks: ")

    # Check if the word exists in the sentence
    while word_to_mask not in sentence:
        word_to_mask = input("Enter the word you want to mask with asterisks: ")

    # Create a string of asterisks with the same length as the word to mask
    asterisks = len(word_to_mask) * "*"

    # Replace occurrences of the word with the asterisks in the sentence
    sentence = sentence.replace(word_to_mask, asterisks)

    # Print the modified sentence
    print(sentence)


if __name__ == "__main__":
    main()  # Call the main function when the script is executed.
