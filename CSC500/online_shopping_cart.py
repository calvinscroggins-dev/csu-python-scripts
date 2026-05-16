# This class represents an item in a shopping cart.
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


# This class represents the customer's shopping cart.
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    choice = ""

    while choice != "q":
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("Choose an option:\n")

        while choice not in ["a", "r", "c", "i", "o", "q"]:
            choice = input("Choose an option:\n")

        if choice == "a":
            print("\nADD ITEM TO CART")

            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_price = float(input("Enter the item price:\n"))
            item.item_quantity = int(input("Enter the item quantity:\n"))

            cart.add_item(item)

        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")

            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_quantity = int(input("Enter the new quantity:\n"))

            cart.modify_item(item)

        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)


if __name__ == "__main__":
    main()