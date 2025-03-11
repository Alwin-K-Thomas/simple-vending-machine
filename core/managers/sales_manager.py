""" Module to handle the sales for vending machine
"""
class SalesManager:
    """ Class to handle the sales and related information for the vending machine
    """
    def __init__(self):
        """ Initiliase for calculation total and product sales.
        """
        self._total_sales = 0
        self._product_sales = {}

    def update_sale(self, product_name, quantity, total_price):
        """ Update the sales data based on the purchase

            Args:
                product_name (name): Name of the product to be updated for sales
                quantity (int): The number of products purchased
                total_price (int): Total amount for the sales.
        """
        if quantity <= 0:
            raise ValueError("Quantity sold must be positive.")
        if total_price <= 0:
            raise ValueError("Total price must be positive.")

        # Update total sales amount
        self._total_sales += total_price

        # Update individual product sales
        if product_name in self._product_sales:
            self._product_sales[product_name]['quantity'] += quantity
            self._product_sales[product_name]['revenue'] += total_price
        else:
            self._product_sales[product_name] = {'quantity': quantity, 'revenue': total_price}

    @property
    def total_sales(self):
        """ Return the total sales amount
        """
        return self._total_sales

    @property
    def product_sales(self):
        """ Return the product sales for each of the products.
        """
        return self._product_sales
