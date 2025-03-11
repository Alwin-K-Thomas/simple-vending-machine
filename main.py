""" Module to handle the CLI interface of the vending machine
"""
from core.controllers.machine_controller import MachineController


def display_products(controller):
    """ Display available products with prices and stock.

        Args:
            controller (MachineController): The manager for the vending machine.
    """
    products = controller.get_all_products()
    print("\nAvailable Products:")
    for product in products:
        print(f"- {product['name']}: {product['price']} coins ({product['stock']} in stock)")


def main():
    """ Main Function for Vending Machine CLI
    """
    # Get the main manager for the vending machine.
    controller = MachineController()

    while True:
        print("\nOptions:")
        print("1. Insert Coins")
        print("2. Purchase Product")
        print("3. View Admin Report")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        # Logic to handle coins in a vending machine
        if choice == "1":
            while True:
                try:
                    coin = int(input(
                        "Insert coin (Accepted: 1, 2, 5, 10). Press 0 to stop: "
                    ).strip())
                    if coin == 0:
                        break
                    controller.insert_coin(coin)
                    print(f"Total Inserted: {controller.inserted_total} coins")

                except ValueError:
                    print("Invalid input. Please insert a valid coin.")

        # Logic to handle the purchase in a vending machine
        elif choice == "2":
            display_products(controller)
            print(f"\nAvailable Balance: {controller.inserted_total} coins")

            try:
                product_name = input("Enter the product name to purchase: ").strip()
                quantity = int(input("Enter the quantity to purchase: ").strip())

                total_cost = controller.inventory_manager.products[product_name].price * quantity
                if controller.inserted_total < total_cost:
                    print("Insufficient balance. Insert more coins.")
                    continue

                # Process the purchase for the chosen products.
                result = controller.purchase_product(
                    product_name, quantity,
                    controller.inserted_total
                )
                if result["success"]:
                    # Deduct the total cost from the inserted amount.
                    remaining_amount = controller.inserted_total - total_cost

                    # Handle the outputs after purchase
                    print(f"Success: {result['message']}")
                    print(f"Change returned: {result['change'] if result['change'] else '0'}")
                    print(f"Remaining Balance: {remaining_amount} coins")

                    # Reset the coins as it is returned
                    controller.inserted_total = 0
                else:
                    print(f"Error: {result['message']}")

            except ValueError:
                print("Invalid input. Please enter correct values.")
            except KeyError:
                print("Invalid product name. Please select from the available products.")

        # Logic for the inventory and sales report.
        elif choice == "3":
            report = controller.get_admin_report()
            print("\nAdmin Report:")
            print(report)

        # Exit logic
        elif choice == "4":
            print("Exiting. Thank you!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
