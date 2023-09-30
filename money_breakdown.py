def main():
    # Prompt the user to input the amount.
    amount = int(input("Enter the amount: "))

    # Break down the amount into denominations.
    breakdown = break_down(amount)

    print(f"The amount {amount} can be broken down into: ")
    for banknote, count in breakdown.items():
        print(f"{count} x {banknote}€")


def break_down(amount):
    # Define the available banknote denominations.
    banknotes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    breakdown = {}

    if not amount:
        print("Invalid input!")
        exit()

    for banknote in banknotes:
        result = amount // banknote
        amount %= banknote
        if result:
            breakdown[banknote] = result

    return breakdown


if __name__ == "__main__":
    main()
