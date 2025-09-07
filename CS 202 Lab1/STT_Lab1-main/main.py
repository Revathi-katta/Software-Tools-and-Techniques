"""
A simple number comparison script.
This script asks the user for two numbers (a and b),
compares them, and prints whether a > b, a == b, or a < b.
"""

def get_number(prompt):
    """Prompt the user to enter a number and return it as a float."""
    while True:
        try:
            value= float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_numbers(a_value, b_value):
    """Compare two numbers and return the comparison result as a string."""
    if a_value > b_value:
        return f"{a_value} is greater than {b_value}"
    if a_value < b_value:
        return f"{a_value} is less than {b_value}"
    return f"{a_value} is equal to {b_value}"


def display_result(result):
    """Display the comparison result."""
    print("\nComparison Result:")
    print(result)


def main():
    """Main function to run the number comparison program."""
    print("Number Comparison Tool")
    print("-" * 25)

    number_a = get_number("Enter the first number (a): ")
    number_b = get_number("Enter the second number (b): ")

    result = compare_numbers(number_a, number_b)

    display_result(result)

    print("\nThank you for using the Number Comparison Tool.")

if __name__ == "__main__":
    main()
