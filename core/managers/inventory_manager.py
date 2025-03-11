""" Module to handle the Inventory for vending machine
"""
from core.models.product import Product


class InventoryManager:
    """ Class to handle all the inventory for vending machine
    """
    def __init__(self, products, sell_ratio, total_inventory):
        """ Intialise the product and inventory sell-ratio

            Args:
                products (list): Products available in the vending machine.
                sell_ratio (list/tuple): Ratio to determine the stock for each product
                total_inventory (int): Total count of the stock available
        """
        self._total_inventory = total_inventory
        self._sell_ratio = sell_ratio
        self._products = {
            product["name"]: Product(product["name"], product["price"], 0)
                 for product in products
        }
        self._setup_inventory()

    @property
    def products(self):
        """ Return all the products
        """
        return self._products

    def _setup_inventory(self):
        """ Setup the inventotu and update the stock based on sell-ratio
        """
        total_count = sum(self._sell_ratio)

        # Update the stock based on the given sell-ratio from the config.
        for idx, product_name in enumerate(self._products):
            stock = int((self._sell_ratio[idx] / total_count) * self._total_inventory)
            self._products[product_name].update_stock(stock)

    def update_stock(self, product_name, quantity):
        """ Update the stock count based on the purchase information

            Args:
                product_name (name): The product to be updated
                quantity (int): The number of the given products to be updated.
        """
        if product_name in self._products:
            self._products[product_name].update_stock(quantity)
        else:
            raise ValueError(f"Product {product_name} not found in inventory.")

    def get_inventory_report(self):
        """ Get the product and its stock information.
        """
        return {name: product.stock for name, product in self._products.items()}
