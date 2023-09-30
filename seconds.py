def main():
    seconds = []

    # Prompt the user to enter 5 sets of seconds.
    for _ in range(0, 5):
        seconds.append(int(input("Enter seconds: ")))

    # Convert and display each set of seconds into days, hours, minutes, and seconds.
    for x in seconds:
        result = convert_seconds(x)
        print(
            f"{x} seconds = {result[0]} days, {result[1]} hours, {result[2]} minutes, and {result[3]} seconds."
        )


def convert_seconds(seconds):
    # Initialize variables to store days, hours, and minutes.
    days = 0
    hours = 0
    minutes = 0

    # Convert seconds to days, hours, and minutes.
    while seconds - 86400 >= 0:
        days += 1
        seconds -= 86400
    while seconds - 3600 >= 0:
        hours += 1
        seconds -= 3600
    while seconds - 60 >= 0:
        minutes += 1
        seconds -= 60

    return [days, hours, minutes, seconds]


if __name__ == "__main__":
    main()
