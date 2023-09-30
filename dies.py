import random

# Initialize variables for two dice and a list to store attempts.
die1 = 0
die2 = 0
attempts = []

# Perform 1001 attempts.
for _ in range(1001):
    attempt_count = 0

    # Keep rolling two dice until they match.
    while True:
        attempt_count += 1

        # Roll two dice.
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        # If the two dice match, exit the loop.
        if die1 == die2:
            break

    # Add the number of attempts for this trial to the list.
    attempts.append(attempt_count)

# Calculate and print the average number of attempts.
average_attempts = sum(attempts) / 1000
print(f"The average number of attempts was: {average_attempts}")
