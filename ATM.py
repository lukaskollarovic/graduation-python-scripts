def main():
    user = {}  # Create an empty user dictionary to store account information.

    card_number = int(input("Enter the card number: "))

    # Match the card number to a user's account or print an error message if not found.
    match card_number:
        case 1111111111111111:
            user = {
                "name": "Peter",
                "gender": "male",
                "PIN": 1111,
                "balance": 10000,
                "attempts": 3,
            }
        case 2222222222222222:
            user = {
                "name": "Viera",
                "gender": "female",
                "PIN": 2222,
                "balance": 20000,
                "attempts": 3,
            }
        case 3333333333333333:
            user = {
                "name": "Filip",
                "gender": "male",
                "PIN": 3333,
                "balance": 30000,
                "attempts": 3,
            }
        case _:
            print("Account not found!")
            quit()

    pin = 0

    while pin != user["PIN"]:
        pin = int(input("Enter your PIN: "))  # Prompt the user to enter their PIN.
        user["attempts"] -= 1  # Decrement the remaining attempts.

        if user["attempts"] == 0:
            print("Account blocked!")
            quit()

    print("-----------------------------")

    if user["gender"] == "female":
        print(f"Welcome, Mrs. {user['name']}!\n")
    else:
        print(f"Welcome, Mr. {user['name']}!\n")

    while True:
        choice = menu()  # Display the menu and get the user's choice.

        if choice == "x":
            exit_program()  # If the user chooses to exit, call the exit_program function.

        elif choice == "s":
            display_balance(
                user
            )  # If the user chooses to check balance, call the display_balance function.

        elif choice == "w":
            withdraw_funds(
                user
            )  # If the user chooses to withdraw funds, call the withdraw_funds function.

        elif choice == "d":
            deposit_funds(
                user
            )  # If the user chooses to deposit funds, call the deposit_funds function.

        else:
            unknown_option()  # If the user selects an unknown option, call the unknown_option function.


def menu():
    # Display the menu options and return the user's choice.
    print("To check your balance, press 's'")
    print("To withdraw funds, press 'w'")
    print("To deposit funds, press 'd'")
    print("To exit, press 'x'")

    option = input("")  # Get the user's input.
    print("-----------------------------")

    return option


def exit_program():
    # Display a goodbye message and exit the program.
    print("Goodbye! Have a nice day!")
    quit()


def display_balance(user):
    # Display the user's account balance.
    print("Your account balance is €" + str(user["balance"]))
    print("-----------------------------")


def withdraw_funds(user):
    # Prompt the user to enter the amount to withdraw and update the balance.
    amount = int(input("Enter the amount to withdraw: "))
    user["balance"] -= amount
    print("-----------------------------")


def deposit_funds(user):
    # Prompt the user to enter the amount to deposit and update the balance.
    amount = int(input("Enter the amount to deposit: "))
    user["balance"] += amount
    print("-----------------------------")


def unknown_option():
    # Display a message for an unknown option.
    print("I don't recognize that option, please select another one!\n")
    print("-----------------------------")


if __name__ == "__main__":
    main()
