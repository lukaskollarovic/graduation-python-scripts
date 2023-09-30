def main():
    # Prompt the user for weight and height
    weight = int(input("Enter weight (in kilograms): "))
    height = int(input("Enter height (in centimeters): ")) / 100  # Convert to meters

    # Print BMI using the 'evaluate' function
    print(f"Your BMI is: {evaluate(weight, height)}")


def evaluate(weight, height):
    # Calculate BMI value
    bmi = weight / height**2

    # Check the BMI value against some conditions
    if bmi > 24.99:
        return "high"
    elif bmi < 18.5:
        return "low"
    else:
        return "ideal"


if __name__ == "__main__":
    main()  # Call the main function when the script is executed.
