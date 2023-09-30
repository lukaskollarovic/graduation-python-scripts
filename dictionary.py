def main():
    # Initialize an empty dictionary to store translations.
    dictionary = {}

    # Input three Slovak and English word pairs into the dictionary.
    for _ in range(3):
        slovak_word = input("Enter a word in Slovak: ")
        english_word = input("Enter the English translation of the word: ")

        dictionary.update({slovak_word: english_word})

    while True:
        # Prompt the user to enter a word for translation.
        word_to_translate = input("Enter a word to translate: ")

        if word_to_translate == "koniec":
            quit()
        elif word_to_translate in dictionary:
            # If the word is in the dictionary, print the translation.
            print(
                f"The translation of {word_to_translate} is {dictionary[word_to_translate]}."
            )
        else:
            # If the word is not in the dictionary, ask the user for the English translation.
            print(f"I don't know the meaning of {word_to_translate}.")
            english_translation = input(
                f"Enter the English translation of {word_to_translate}: "
            )
            dictionary[word_to_translate] = english_translation


if __name__ == "__main__":
    main()
