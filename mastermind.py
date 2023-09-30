import random

correct = 0
incorrect = 0
response = ""

while True:
    number = random.randint(0, 10)
    print("I've chosen a number, can you guess it?")

    while True:
        response = input("Enter your guess: ")

        if response == "end":
            break

        elif int(response) == number:
            correct += 1
            print(f"Correct! I was thinking of {number}")
            break

        else:
            incorrect += 1
            continue

    if response == "end":
        break

print("Score:")
print(f"Number of correct guesses: {correct}")
print(f"Number of incorrect guesses: {incorrect}")
print(f"Total number of guesses: {correct + incorrect}")
