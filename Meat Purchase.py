def calculate_meal_total():
    try:
        # Get user input
        food_charge = float(input("Enter the charge for the food: $"))

        # Validate input
        if food_charge < 0:
            print("Error: Food charge cannot be negative.")
            return

        # Constants
        TIP_RATE = 0.18
        TAX_RATE = 0.07

        # Calculations
        tip = food_charge * TIP_RATE
        tax = food_charge * TAX_RATE
        total = food_charge + tip + tax

        # Output results
        print("\n--- Meal Cost Breakdown ---")
        print(f"Food Charge: ${food_charge:.2f}")
        print(f"Tip (18%): ${tip:.2f}")
        print(f"Sales Tax (7%): ${tax:.2f}")
        print(f"Total Price: ${total:.2f}")

    except ValueError:
        print("Error: Please enter a valid numeric value.")


# Run the program
calculate_meal_total()