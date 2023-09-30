def main():
    print("\nQuadratic Equation Calculator in R")
    print("ax^2 + bx + c = 0")

    # Prompt the user to input coefficients a, b, and c
    a = float(input("\nEnter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    if a == 0 and b == 0:
        if c != 0:
            print("The quadratic equation becomes a linear one and has no solution.")
        else:
            print(
                "The quadratic equation becomes a linear one and has infinitely many solutions."
            )

    else:
        # Calculate the discriminant
        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            print("The quadratic equation has no real solutions.")
        elif discriminant == 0:
            x = -b / (2 * a)
            print("The quadratic equation has one real solution.")
            print(f"The root of the equation is: {x}.")
        else:
            x1 = (-b + discriminant**0.5) / (2 * a)
            x2 = (-b - discriminant**0.5) / (2 * a)
            print("The quadratic equation has two real solutions.")
            print(f"The roots of the equation are: {x1} and {x2}.")


if __name__ == "__main__":
    main()
