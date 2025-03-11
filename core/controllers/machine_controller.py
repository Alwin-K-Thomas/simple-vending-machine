""" Module to handle the vending machine controller.
"""
from core.config.config_loader import ConfigLoader
from core.managers.admin_report import AdminReport
from core.managers.sales_manager import SalesManager
from core.managers.inventory_manager import InventoryManager
from core.managers.transaction_manager import TransactionManager


class MachineController:
    """ Class to describe the vending machine controls
    """
    def __init__(self):
        """ Setup the config and all managers
        """
        config = ConfigLoader.load_config()
        self.__inserted_total = 0
        self._coins_allowed = config["all_coins"]

        # Initialise all the managers for the vending machine.
        self.inventory_manager = InventoryManager(
            config["all_products"],
            config["sell_ratio"],
            config["total_inventory"]
        )
        self.transaction_manager = TransactionManager(config["all_coins"])
        self.sales_manager = SalesManager()
        self.admin_report = AdminReport(self.inventory_manager, self.sales_manager)

    @property
    def coins_allowed(self):
        """ Returns all the accepted coins
        """
        return self._coins_allowed

    @property
    def inserted_total(self):
        """ Return the total inserted amount.
        """
        return self.__inserted_total

    @inserted_total.setter
    def inserted_total(self, value):
        """
        """
        self.__inserted_total = value

    def get_all_products(self):
        """ Get all the products available inside the vending machine.
        """
        return [
            { "name": name, "price": product.price, "stock": product.stock }
                for name, product in self.inventory_manager.products.items()
        ]

    def purchase_product(self, product_name, quantity, inserted_amount):
        """ Purchase a product from the vending machine
            
            Args:
                product_name (str): Name of the product to be purchased.
                quantity (int): Number of products to be purchased.
                inserted_amount (int): Total amount of coins inserted.
        """
        product = self.inventory_manager.products.get(product_name, None)
        if not product:
            return {"success": False, "message": "Product not found.", "change": inserted_amount}

        # Calculate the total price based on the unit price and quantity
        total_price = product.price * quantity

        # Handle when stocks are less
        if product.stock < quantity:
            return {"success": False, "message": "Insufficient stock.", "change": inserted_amount}

        try:
            change = self.transaction_manager.process_payment(total_price, inserted_amount)
        except ValueError:
            return {"success": False, "message": "Insufficient funds.", "change": inserted_amount}

        # Update the stock after purchase.
        self.inventory_manager.update_stock(product_name, -quantity)
        self.sales_manager.update_sale(product_name, quantity, total_price)
        # Resetting the amount as it is now

        return {
            "success": True,
            "message": f"Purchased {quantity} {product_name}(s).", "change": change
        }

    def insert_coin(self, coin):
        """ Handle the insertion of coins based on the accepted coin denominations.

            Args:
                coin (int): The coin which is inserted into the machine.
        """
        if coin in self._coins_allowed:
            self.__inserted_total += coin
        else:
            print(f"Machine doesn't accept {coin} units. Please insert 1, 2, 5, or 10 coins.")

    def get_admin_report(self):
        """ To generate the report of sales and inventory.
        """
        return self.admin_report.generate_report()
