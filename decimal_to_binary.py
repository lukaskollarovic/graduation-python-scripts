def main():
    # Create a list of numbers.
    number_list = [10, 56, 125, 98]

    for number in number_list:
        # Convert each number to its binary representation and print it.
        print(to_binary(number))


def to_binary(num):
    binary_str = ""

    # Convert the number to its binary representation.
    while num > 0:
        binary_str += str(num % 2)
        num = num // 2

    # Reverse the binary string to get the correct representation.
    return binary_str[::-1]


if __name__ == "__main__":
    main()
