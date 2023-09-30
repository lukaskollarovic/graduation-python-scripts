def main():
    # Declare an empty list.
    numberList = []

    # Programatically fill the list with binary values.
    for _ in range(3):
        numberList.append(input("Enter a number in binary format: "))

    # Convert each number in the list to decimal.
    for number in numberList:
        print(to_decimal(number))


def to_decimal(number):
    # Declare a variable to store the decimal value.
    decimalValue = 0
    # Store the length of the number (used in conversion).
    length = len(number)

    # Convert each digit of the binary number to decimal using the formula.
    for digit in number:
        digit = int(digit) * (2 ** (length - 1))  # Starts at 0, so use length - 1.
        decimalValue += digit
        length -= 1  # Move to the next digit.

    return decimalValue


if __name__ == "__main__":
    main()
