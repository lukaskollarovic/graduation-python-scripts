import random
import itertools


def main():
    # Define character sets for generating passwords.
    characters1 = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    characters2 = ["a", "b", "c", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Generate passwords and find the number of attempts needed to guess them.
    attempts1 = find_password_attempts(gen_password1(characters1), characters1)
    attempts2 = find_password_attempts(gen_password2(characters2), characters2)

    # Compare the security of passwords based on the number of attempts needed.
    if attempts1 > attempts2:
        print(
            f"With {attempts1} attempts, a shorter password with more characters is more secure!"
        )
    else:
        print(
            f"With {attempts2} attempts, a longer password with fewer characters is more secure!"
        )


def gen_password1(characters):
    # Generate a password with 3 characters randomly chosen from the given character set.
    password = ""

    for i in range(3):
        password += random.choice(characters)

    return password


def gen_password2(characters):
    # Generate a password with 6 characters randomly chosen from the given character set.
    password = ""

    for i in range(6):
        password += random.choice(characters)

    return password


def find_password_attempts(password, characters):
    # Generate all possible combinations of characters for the given password length.
    combinations = itertools.product(characters, repeat=len(password))
    attempts = 0

    # Iterate through combinations and count attempts until the password is found.
    for combination in combinations:
        attempts += 1

        combination = "".join(combination)

        if combination == password:
            return attempts


if __name__ == "__main__":
    main()
