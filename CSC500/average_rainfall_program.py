# Average Rainfall Program

# Initialize variables
total_rainfall = 0
total_months = 0

# Ask user for number of years
years = int(input("Enter the number of years: "))

# Validate years input
while years <= 0:
    print("Error: Number of years must be greater than 0.")
    years = int(input("Enter the number of years: "))

# Outer loop for years
for year in range(1, years + 1):

    print(f"\nYear {year}")

    # Inner loop for 12 months
    for month in range(1, 13):

        # Ask user for monthly rainfall
        monthly_rainfall = float(
            input(f"Enter rainfall for month {month} in inches: ")
        )

        # Validate rainfall input
        while monthly_rainfall < 0:
            print("Error: Rainfall cannot be negative.")
            monthly_rainfall = float(
                input(f"Re-enter rainfall for month {month}: ")
            )

        # Add rainfall to total
        total_rainfall += monthly_rainfall
        total_months += 1

# Calculate average rainfall
average_rainfall = total_rainfall / total_months

# Display results
print("\nRainfall Statistics")
print(f"Total Months: {total_months}")
print(f"Total Rainfall: {total_rainfall:.2f} inches")
print(f"Average Rainfall Per Month: {average_rainfall:.2f} inches")