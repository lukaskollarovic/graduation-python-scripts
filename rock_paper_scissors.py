import random


def main():
    attempts = 0
    wins = 0

    while True:
        player1 = random.randint(1, 3)  # 1 = rock, 2 = paper, 3 = scissors
        player2 = random.randint(1, 3)

        attempts += 1

        if player1 != player2:  # Check if it's not a tie
            if isPlayer1Winner(player1, player2):
                wins += 1

        probability = wins / attempts * 100

        if attempts > 1 and probability >= 33:
            print(f"A 33% success rate was achieved after {attempts} attempts.")
            break


def isPlayer1Winner(player1, player2):
    # Define the winning conditions for player1
    # Player1 wins if they choose "rock" (1) and player2 chooses "scissors" (3)
    # Player1 wins if they choose "paper" (2) and player2 chooses "rock" (1)
    # Player1 wins if they choose "scissors" (3) and player2 chooses "paper" (2)
    return (
        (player1 == 1 and player2 == 3)
        or (player1 == 2 and player2 == 1)
        or (player1 == 3 and player2 == 2)
    )


if __name__ == "__main__":
    main()
