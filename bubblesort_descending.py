def main():
    # Create an empty list to store numbers.
    numbers = []

    # Prompt the user to input 10 numbers and add them to the list.
    for _ in range(10):
        numbers.append(int(input("Enter a number: ")))

    # Call the 'sort_descending' function to sort the numbers in descending order.
    sorted_numbers = sort_descending(numbers)

    # Print the sorted numbers as a comma-separated string.
    print(", ".join(map(str, sorted_numbers)))


def sort_descending(numbers):
    # Use the bubble sort algorithm to sort the numbers in descending order.

    while True:
        swaps = 0

        for i in range(0, len(numbers) - 1):
            # Compare adjacent numbers and swap them if they are in the wrong order (descending).
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swaps += 1

        # If no swaps were made in a pass, the list is sorted in descending order.
        if swaps == 0:
            return numbers


if __name__ == "__main__":
    main()  # Call the main function when the script is executed.
