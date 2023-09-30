def main():
    # Prompt the user to input the first number.
    first = int(input("First number: "))
    # Prompt the user to input the second number.
    second = int(input("Second number: "))

    # Calculate and print the greatest common divisor (GCD) using the Euclidean algorithm.
    print(
        f"The greatest common divisor of {first} and {second} is {euclidean(first, second)}."
    )


def euclidean(a, b):
    # Implement the Euclidean algorithm to find the greatest common divisor (GCD).
    while a != b:
        if a > b:
            a = a - b
        else:
            a, b = b, a
    return a


# Call the main function to start the program.
if __name__ == "__main__":
    main()
