def format_result(value):
    return int(value) if value.is_integer() else value

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
multiplication = num1 * num2

# Handle division safely
if num2 != 0:
    division = num1 / num2
else:
    division = None

# Display results
print("\nResults:")
print("Multiplication:", format_result(multiplication))

if division is None:
    print("Division: Cannot divide by zero")
else:
    print("Division:", format_result(division))