def format_result(value):
    return int(value) if value.is_integer() else value

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2

# Display results
print("\nResults:")
print("Addition:", format_result(addition))
print("Subtraction:", format_result(subtraction))