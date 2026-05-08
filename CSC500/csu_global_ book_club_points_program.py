# CSU Global Book Club Points Program

# Ask user for number of books purchased
books_purchased = int(
    input("Enter the number of books purchased this month: ")
)

# Validate input
while books_purchased < 0:
    print("Error: Number of books cannot be negative.")
    books_purchased = int(
        input("Re-enter the number of books purchased: ")
    )

# Determine points earned
if books_purchased >= 8:
    points = 60
elif books_purchased >= 6:
    points = 30
elif books_purchased >= 4:
    points = 15
elif books_purchased >= 2:
    points = 5
else:
    points = 0

# Display points earned
print(f"You earned {points} points.")