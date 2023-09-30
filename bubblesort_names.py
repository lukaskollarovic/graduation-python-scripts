def main():
    # Initialize an empty list to store names
    names = []

    # Prompt the user to input 5 names and add them to the list
    for _ in range(0, 5):
        names.append(input("Enter a name: "))

    # Call the 'sort_names' function to sort the list
    sorted_names = sort_names(names)

    # Print the sorted names
    for x in sorted_names:
        print(x)


def sort_names(names):
    # This function performs bubble sort on the list of names

    while True:
        swaps = 0

        # Iterate through the list and compare adjacent names
        for i in range(0, len(names) - 1):
            if names[i] > names[i + 1]:
                # If the current name is greater than the next name, swap them
                names[i], names[i + 1] = names[i + 1], names[i]
                swaps += 1

        # If no swaps were made in a pass, the list is sorted
        if swaps == 0:
            return names


if __name__ == "__main__":
    main()  # Call the main function when the script is executed.
