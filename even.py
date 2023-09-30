def main():
    # Open the original file for reading
    original_file = open("numbers.txt")
    print(original_file)  # Print the file object (not the content)

    # Open a new file for writing even numbers
    new_file = open("even.txt", "w")

    # Iterate through each line in the original file
    for line in original_file:
        # Check if the number (converted from a string to an integer) is even
        if int(line) % 2 == 0:
            # Write the even number to the new file
            new_file.write(line)

    # Close both files when done
    original_file.close()
    new_file.close()


if __name__ == "__main__":
    main()  # Call the main function when the script is executed.
