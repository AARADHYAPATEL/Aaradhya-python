import random

# a class to represent an order

class Order:
    def __init__(self, order_id, item_name, quantity):
        self.order_id = order_id
        self.item_name = item_name
        self.quantity = quantity
        self.status = "pending"

# Main application class

class OrderTrackingApp:
    def __init__(self):
        self.orders = []

    # place a new order

    def place_order(self):
        order_id = random.randint(1000, 9999)
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        order = Order(order_id, item_name, quantity)
        self.orders.append(order)
        print(f"Order placed successfully. Order ID is {order_id}")

    # View all orders

    def view_orders(self):
        if not self.orders:
            print("No orders found")
        else:
            print("\n Current Orders:")

            for order in self.orders:
                print(f"Order ID: {order.order_id}, Item: {order.item_name}, Quantity: {order.quantity}, Status: {order.status}")

    # Track a specific order by ID

    def track_order(self):
        order_id = int(input("Enter order ID: "))
        for order in self.orders:
            if order.order_id == order_id:
                print(f"Order ID: {order.order_id}, Item: {order.item_name}, Quantity: {order.quantity}, Status: {order.status}")
                return
        print("Order not found")

    # Update the status of an order

    def update_order_status(self):
        order_id = int(input("Enter order ID: "))
        for order in self.orders:
            if order.order_id == order_id:
                new_status = input("Enter new status(Pending, Shipped, Delivered): ")
                order.status = new_status
                print(f"Order {order_id} status updated to {new_status}")
                return
        print("Order not found")

# Main function

def main():
    app = OrderTrackingApp()

    while True:
        print("\n--- Order Tracking System ---")
        print("1. Place Order")
        print("2. View Orders")
        print("3. Track Order")
        print("4. Update Order Status")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            app.place_order()
        elif choice == 2:
            app.view_orders()
        elif choice == 3:
            app.track_order()
        elif choice == 4:
            app.update_order_status()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()