""" Module to handle the products in the vending machine
"""
class Product:
    """ Class to represent a product in the vending machine.
    """
    def __init__(self, name, price, stock):
        """ Initialise the attributes for a product
        """
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """ Updates the stock of the product.

            Args:
                quantity (int): Number of quantities to be updated for
                    a product.
        """
        if self.stock + quantity < 0:
            raise ValueError(f"Insufficient stock for {self.name}.")

        self.stock += quantity
