def main():
    # Create an empty dictionary to store people's names and birth years.
    people = {}

    # Prompt the user to input names and birth years for three people.
    for _ in range(3):
        name = input("Enter a name: ")
        birth_year = int(input("Enter the birth year: "))

        # Add the name and birth year to the dictionary.
        people.update({name: birth_year})

    # Print the youngest and oldest person using the 'findYoungest' and 'findOldest' functions.
    print(f"The youngest person is: {findYoungest(people)}")
    print(f"The oldest person is: {findOldest(people)}")


def findYoungest(dictionary):
    # Find the highest birth year (youngest) among the values in the dictionary.
    highest = max(dictionary.values())

    # Iterate through the dictionary keys to find the person with the highest birth year.
    for name in dictionary.keys():
        if dictionary[name] == highest:
            return name  # Return the name of the youngest person.


def findOldest(dictionary):
    # Find the lowest birth year (oldest) among the values in the dictionary.
    lowest = min(dictionary.values())

    # Iterate through the dictionary keys to find the person with the lowest birth year.
    for name in dictionary.keys():
        if dictionary[name] == lowest:
            return name  # Return the name of the oldest person.


if __name__ == "__main__":
    main()
