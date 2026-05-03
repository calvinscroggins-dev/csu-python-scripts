# This class represents an item in a shopping cart with a name, price, and quantity.
# It calculates and prints the total cost of the item.
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")


# Create an empty shopping cart list
shopping_cart = []

# Get two items from the user
for i in range(1, 3):
    print(f"Item {i}")

    item = ItemToPurchase()

    item.item_name = input("Enter the item name:\n")
    item.item_price = float(input("Enter the item price:\n"))
    item.item_quantity = int(input("Enter the item quantity:\n"))

    # Store item details in a dictionary
    item_dictionary = {
        "name": item.item_name,
        "price": item.item_price,
        "quantity": item.item_quantity
    }

    # Add the object to the shopping cart list
    shopping_cart.append(item)

    print()


# Display total cost
print("TOTAL COST")

total_cost = 0.0

for item in shopping_cart:
    item.print_item_cost()
    total_cost += item.item_price * item.item_quantity

print(f"\nTotal: ${total_cost:.2f}")