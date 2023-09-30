def main():
    # Prompt the user to input a text containing words and numbers, then split it into a list.
    text = input("Enter a text containing words and numbers: ").split()

    # Initialize lists to separate words and numbers.
    words = []
    numbers = []

    # Iterate through the input text, cleaning and categorizing words and numbers.
    for x in text:
        # Clean the word by making it lowercase and stripping common punctuation.
        x = x.lower().strip(" ,.")

        if x.isalpha():
            # If the cleaned text is alphabetic, add it to the words list.
            words.append(x)
        else:
            # If it's not alphabetic, assume it's a number and convert it to an integer.
            numbers.append(int(x))

    # Print the categorized results.
    print(f"Words: {words}")
    print(f"Numbers: {numbers}")
    print(f"The longest word is: {findMaxWord(words)}")
    print(f"The shortest word is: {findMinWord(words)}")
    print(f"The largest number is: {max(numbers)}")
    print(f"The smallest number is: {min(numbers)}")


def findMaxWord(words):
    # Initialize the longest word as the first word in the list.
    longest_word = words[0]

    # Find the longest word by comparing lengths.
    for x in words:
        if len(x) > len(longest_word):
            longest_word = x

    return longest_word


def findMinWord(words):
    # Initialize the shortest word as the first word in the list.
    shortest_word = words[0]

    # Find the shortest word by comparing lengths.
    for x in words:
        if len(x) < len(shortest_word):
            shortest_word = x

    return shortest_word


if __name__ == "__main__":
    main()
