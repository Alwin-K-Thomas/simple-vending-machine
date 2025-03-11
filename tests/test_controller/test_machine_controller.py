""" Unit tests for machine controller
"""
from io import StringIO
import unittest
from unittest.mock import patch, MagicMock

from core.controllers.machine_controller import MachineController
from core.models.product import Product


class TestMachineController(unittest.TestCase):
    """ Test class for Machine controller in vending machine.
    """
    def setUp(self):
        """ Setup for tests
        """
        self.controller = MachineController()

        # Creating mock managers
        self.controller.inventory_manager = MagicMock()
        self.controller.transaction_manager = MagicMock()
        self.controller.sales_manager = MagicMock()
        self.controller.admin_report = MagicMock()

    def test_initial_config(self):
        """ Test to confirm the setup for controller
        """
        self.assertEqual(self.controller.inserted_total, 0)
        self.assertEqual(self.controller.coins_allowed, [1, 2, 5, 10])

    def test_insert_coin_valid_coin(self):
        """ Test to confirm that we can accept a valid coin
        """
        self.controller.insert_coin(1)
        self.assertEqual(self.controller.inserted_total, 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_insert_coin_invalid_coin(self, mock_stdout):
        """ Test to confirm the rejection of an invalid coin.
        """
        self.controller.insert_coin(3)
        print_out = mock_stdout.getvalue()
        self.assertIn(
            "Machine doesn't accept 3 units. Please insert 1, 2, 5, or 10 coins.",
            print_out
        )

    def test_purchase_success(self):
        """ Test to confirm the successful purchase of a product.
        """
        product = Product("Product1", 1.5, 10)

        # Setup the mock product
        self.controller.inventory_manager.products = {"Product1": product}
        self.controller.inserted_total = 5
        self.controller.transaction_manager.process_payment.return_value = [1, 1, 1]

        result = self.controller.purchase_product("Product1", 2, 5)

        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Purchased 2 Product1(s).")
        self.assertEqual(result["change"], [1, 1, 1])

    def test_purchase_insufficient_funds(self):
        """ Test to confirm that we can't purchase without sufficient funds.
        """
        product = Product("Product1", 1.5, 10)
         # Setup the mock product
        self.controller.inventory_manager.products = {"Product1": product}
        self.controller.inserted_total = 2
        self.controller.transaction_manager.process_payment = MagicMock(
            side_effect=ValueError("Insufficient funds")
        )
        result = self.controller.purchase_product("Product1", 2, 2)

        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Insufficient funds.")
        self.assertEqual(result["change"], 2)
    
    def test_purchase_product_not_listed(self):
        """ Test to confirm that vending machine handles when
            we try to purchase a product which is not listed.
        """
        self.controller.inventory_manager.products = MagicMock()
        self.controller.inventory_manager.products.get.return_value = None

        # Trying to purchase a product which doesn't exists
        result = self.controller.purchase_product("RandomProduct", 2, 5)

        # This should fail with "product not found" message
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Product not found.") 
        self.assertEqual(result["change"], 5)

    def test_purchase_product_not_found(self):
        """ Test to confirm that we can't purchase a product which is
            out of stock.
        """
        product = Product("Product", 1.5, 1)
        self.controller.inventory_manager.products = {"Product": product}
        self.controller.inserted_total = 5

        # Trying to purchase 2 Products, but only 1 is available
        result = self.controller.purchase_product("Product", 2, 5)

        # It should fail with insufficient stock message
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Insufficient stock.")
        self.assertEqual(result["change"], 5)

    def test_get_all_products(self):
        """ Test to confirm the listing of all products
        """
        # Create mock products
        product_1 = Product("Product1", 1.5, 10)
        product_2 = Product("Product2", 2.0, 5)

        self.controller.inventory_manager.products = {
            "Product1": product_1,
            "Product2": product_2
        }

        # Get all products
        result = self.controller.get_all_products()

        self.assertEqual(len(result), 2)
    
    def test_get_admin_report(self):
        """ Test to confirm the admin report generation.
        """
        # Mock the generate_report method
        self.controller.admin_report.generate_report = MagicMock(
            return_value="Generate data"
        )

        result = self.controller.get_admin_report()

        # Confirm it is called and returned correctly.
        self.assertEqual(result, "Generate data")
        self.controller.admin_report.generate_report.assert_called_once()

if __name__ == '__main__':
    unittest.main()
