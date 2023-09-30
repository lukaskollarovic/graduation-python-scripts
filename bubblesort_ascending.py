def main():
    numbers = []

    # Prompt the user to enter 10 numbers and add them to the list.
    for _ in range(0, 10):
        numbers.append(int(input("Enter a number: ")))

    # Call the 'sort_numbers' function to sort the list.
    sorted_numbers = sort_numbers_ascending(numbers)

    # Print the sorted numbers as a comma-separated string.
    print("Sorted numbers: " + ", ".join(map(str, sorted_numbers)))


def sort_numbers_ascending(numbers):
    while True:
        swaps = 0

        # Iterate through the list and compare adjacent numbers.
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                # If the current number is greater than the next number, swap them.
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swaps += 1

        # If no swaps were made in a pass, the list is sorted in ascending order.
        if swaps == 0:
            return numbers


if __name__ == "__main__":
    main()  # Call the main function when the script is executed.
