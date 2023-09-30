def main():
    # Print the results of the 'division' and 'multiplication' functions.
    print(division(6, 3))
    print(multiplication(2, 3))


def division(dividend, divisor):
    quotient = 0

    # Perform integer division while the dividend is not zero.
    while dividend != 0:
        dividend -= divisor  # Subtract the divisor from the dividend.
        quotient += 1  # Increment the quotient.

    return quotient  # Return the result.


def multiplication(factor1, factor2):
    product = factor1  # Initialize the product with the first factor.

    # Loop to add the first factor to itself 'factor2-1' times.
    for _ in range(1, factor2):
        product += factor1  # Add the first factor to the product.

    return product  # Return the result.


if __name__ == "__main__":
    main()  # Call the main function when the script is executed.
