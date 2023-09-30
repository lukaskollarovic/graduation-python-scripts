def main():
    # Prompt the user to input text they want to censor.
    text = input("Enter the text you want to censor: ").split()

    # Prompt the user to input words in the format "apple, car,.." that they want to censor.
    words = input(
        "Enter words in the format 'apple, car,..' that you want to censor: "
    ).split(", ")

    # Censor the text and print the result.
    censored_text = censor(text, words)
    print(censored_text)


def censor(text, words):
    censored_text = ""

    for word in text:
        if word in words:
            # If the word is in the list of words to censor, replace it with asterisks of the same length.
            censored_text += len(word) * "*" + " "
        else:
            # If the word is not in the list, keep it unchanged.
            censored_text += word + " "

    return censored_text


if __name__ == "__main__":
    main()
