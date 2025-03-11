""" Unit tests for the Inventory Manager.
"""
import unittest

from core.managers.inventory_manager import InventoryManager
from core.models.product import Product


class TestInventoryManager(unittest.TestCase):
    """ Test for inventory manager.
    """
    def setUp(self):
        """ Setting up the mock products.
        """
        products = [{"name": "Product", "price": 2}]
        sell_ratio = [1]
        total_inventory = 10
        self.manager = InventoryManager(
            products,
            sell_ratio,
            total_inventory
        )

    def test_update_stock_positive(self):
        """ Test to confirm the update of stock by adding products.
        """
        self.manager.update_stock("Product", 5)
        self.assertEqual(self.manager.products["Product"].stock, 15)

    def test_update_stock_negative(self):
        """ Test to confirm the update of stock by removing products.
        """
        self.manager.update_stock("Product", -3)
        self.assertEqual(self.manager.products["Product"].stock, 7)

    def test_update_stock_not_found(self):
        """ Test to confirm that we can't update a product stock
            which is not available or listed
        """
        with self.assertRaises(ValueError):
            self.manager.update_stock("NonExistentProduct", 10)

    def test_update_stock_empty(self):
        """ Test to confirm that we can't update a stock after
            emptying the product. (below 0)
        """
        with self.assertRaises(ValueError):
            self.manager.update_stock("Product", -11)

    def test_get_inventory_report(self):
        """ Test to confirm that we can generate inventory report.
        """
        self.manager.update_stock("Product", 8)

        # Call the get_inventory_report method
        report = self.manager.get_inventory_report()

        # Assertions to check if the report contains correct stock counts
        self.assertEqual(report["Product"], 18)  # After update, stock should be 8

if __name__ == '__main__':
    unittest.main()
