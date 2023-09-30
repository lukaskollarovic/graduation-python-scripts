def main():
    # Prompt the user to input a Roman numeral.
    roman_numeral = input("Enter a number in Roman numeral format: ")

    # Print the converted number and call the function.
    print(f"Your number in Arabic numeral format is: {roman_to_arabic(roman_numeral)}")


def roman_to_arabic(roman_numeral):
    # Initialize a dictionary of numeral values.
    numeral_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Declare a variable to store the converted number.
    arabic_number = 0

    # Sum the values of the characters (if input is correct).
    for character in roman_numeral:
        if character in numeral_dict:
            arabic_number += numeral_dict[character]

    # Perform adjustment by subtracting values when a smaller value precedes a larger value.
    # (This needs to be subtracted once, but we added it earlier, so we subtract it twice.)
    for i in range(1, len(roman_numeral)):
        if numeral_dict[roman_numeral[i - 1]] < numeral_dict[roman_numeral[i]]:
            arabic_number -= 2 * numeral_dict[roman_numeral[i - 1]]

    return arabic_number


if __name__ == "__main__":
    main()
