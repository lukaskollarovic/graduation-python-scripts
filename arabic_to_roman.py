# Define a dictionary that maps Arabic numerals to Roman numerals.
numeral_system = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

# Prompt the user to input an Arabic numeral.
arabic = int(input("Enter a number: "))

# Initialize an empty string to store the Roman numeral representation.
roman = ""

# Convert the Arabic numeral to Roman numeral.
for numeral in numeral_system:
    count = arabic // numeral
    arabic %= numeral

    # Append the corresponding Roman numeral to the result string.
    for _ in range(count):
        roman += numeral_system[numeral]

# Print the Roman numeral representation.
print(roman)
