class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class CoffeeShop:
    def __init__(self):
        self.coffees = [
            Coffee("Espresso", 2.50),
            Coffee("Latte", 3.00),
            Coffee("Cappuccino", 3.50),
            Coffee("Americano", 3.75),
            Coffee("Mocha", 4.00)
        ]
        self.orders = []

    def display_menu(self):
        print("\nAvailable coffees:")
        for index, coffee in enumerate(self.coffees):
            print(f"{index + 1}. {coffee}")

    def take_order(self):
        while True:
            self.display_menu()
            choice = input("Enter the number of the coffee you'd like to order (select 'q' to quit): ")
            if choice.lower() == 'q':
                break
            try:
                coffee_index = int(choice) - 1
                if 0 <= coffee_index < len(self.coffees):
                    self.orders.append(self.coffees[coffee_index])
                    print(f"Added {self.coffees[coffee_index].name} to your order.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter 'q' to quit or a number to order a coffee.")

    def calculate_total(self):
        return sum(coffee.price for coffee in self.orders)

    def display_order(self):
        if not self.orders:
            print("You haven't ordered anything yet.")
            return
        print("\nYour order:")
        for coffee in self.orders:
            print(f"- {coffee}")
        total = self.calculate_total()
        print(f"Total amount due: ${total:.2f}")

    def confirm_order(self):
        while True:
            self.display_order()
            confirm = input("Confirm order? (y/n): ")
            if confirm.lower() == 'y':
                print("Thank you for your order!")
                break
            elif confirm.lower() == 'n':
                print("Order cancelled. You can place a new order.")
                self.orders.clear()
                break
            else:
                print("Invalid input. Please enter 'y' to confirm or 'n' to cancel.")

    def display_command_menu(self):
        print("\nCommand Menu:")
        print("1. View Coffee menu")
        print("2. Place an order")
        print("3. View your order")
        print("4. Confirm order")
        print("5. Quit")

    def run(self):
        while True:
            self.display_command_menu()
            command = input("Enter the number of the command you'd like to execute (1-5): ")
            if command == '1':
                self.display_menu()
            elif command == '2':
                self.take_order()
            elif command == '3':
                self.display_order()
            elif command == '4':
                self.confirm_order()
            elif command == '5':
                print("Thank you for visiting the Coffee Shop. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    shop = CoffeeShop()
    print("Welcome to the Coffee Shop!")
    shop.run()

if __name__ == "__main__":
    main()