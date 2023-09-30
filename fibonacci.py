def main():
    # Request the range of the Fibonacci sequence.
    range_limit = int(input("Enter the range of the Fibonacci sequence: "))

    for x in range(1, range_limit + 1):
        # Print the Fibonacci sequence up to the specified range.
        print(fibonacci(x))


def fibonacci(r):
    sequence = [1, 1]
    a = 1
    b = 1
    c = 0

    i = 0
    while i != r:
        c = a + b
        sequence.append(c)
        a = b
        b = c

        i += 1

    return sequence


if __name__ == "__main__":
    main()
