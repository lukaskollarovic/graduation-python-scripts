def main():
    # Open the original file for reading in text mode ("rt")
    original_file = open("numbers.txt", "rt")

    # Open a new file for writing (or creating) with the name "odd.txt"
    new_file = open("odd.txt", "w")

    # Iterate through each line in the original file
    for line in original_file:
        # Check if the number (converted from a string to an integer) is odd (remainder when divided by 2 is 1)
        if int(line) % 2 == 1:
            # Write the odd number to the new file
            new_file.write(line)

    # Close the original and new files when done
    original_file.close()
    new_file.close()


if __name__ == "__main__":
    main()
