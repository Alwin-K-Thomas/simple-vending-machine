""" Module to handle the admin report generation.
"""
class AdminReport:
    """ Class which handles the report functionalities.
    """
    def __init__(self, inventory_manager, sales_manager):
        """ Setup the inventory and sales manager to create the report

            Args:
                inventory_manager (InventoryManager): controller which handles
                    the inventory for the vending machine
                sales_manager (SalesManager): controller which handles
                    the sales for the vending machine.
        """
        self.inventory_manager = inventory_manager
        self.sales_manager = sales_manager

    def generate_report(self):
        """ Function to generate the report which contains the inventory,
            and sales report for each product and total sales
        """
        inventory_report = self.inventory_manager.get_inventory_report()
        total_sales = self.sales_manager.total_sales
        product_sales = self.sales_manager.product_sales

        return {
            "inventory": inventory_report,
            "product_sales": product_sales,
            "total_sales": total_sales
        }
