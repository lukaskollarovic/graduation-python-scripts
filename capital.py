def main():
    # Prompt the user for input text and split it into words.
    text = input("Enter text in the format - Today Is GrAduation: ").split(" ")

    # Print the modified text using the 'capitalize_words' function.
    print(capitalize_words(text))


def capitalize_words(text):
    # Initialize a variable to store the capitalized text.
    capitalized_text = ""

    # Iterate through each word in the text.
    for word in text:
        # Capitalize the first letter of each word and convert the rest to lowercase.
        capitalized_word = word.lower().capitalize()

        # Append the capitalized word to the result with a space.
        capitalized_text += capitalized_word + " "

    return capitalized_text


if __name__ == "__main__":
    main()  # Call the main function when the script is executed.
