""" Unit tests for sales manager.
"""
import unittest

from core.managers.sales_manager import SalesManager


class TestSalesManager(unittest.TestCase):
    """ Tests for sale manager module.
    """
    def setUp(self):
        """ Setting up the manager.
        """
        self.manager = SalesManager()

    def test_update_sale(self):
        """ Test to confirm that we can update the sales
        """
        self.manager.update_sale("Product", 2, 3.0)

        self.assertEqual(self.manager.total_sales, 3.0)
        self.assertEqual(self.manager.product_sales["Product"]["quantity"], 2)
        self.assertEqual(self.manager.product_sales["Product"]["revenue"], 3.0)

    def test_update_sale_existing_product(self):
        """ Test to confirm that we can do multile sales
            of the same product.
        """
        self.manager.update_sale("Product", 2, 3.0)
        # Add sales entry again.
        self.manager.update_sale("Product", 3, 4.5)

        # Total sales should be updated
        self.assertEqual(self.manager.total_sales, 7.5)

        # Confirming quantity and revenue for the product.
        self.assertEqual(self.manager.product_sales["Product"]["quantity"], 5)
        self.assertEqual(self.manager.product_sales["Product"]["revenue"], 7.5)

    def test_update_sale_invalid(self):
        """ Test to confirm that we can't purchase a
            negative quantity or negative price.
        """
        with self.assertRaises(ValueError):
            self.manager.update_sale("Product", -1, 3.0)

        with self.assertRaises(ValueError):
            self.manager.update_sale("Product", 2, -3.0)


if __name__ == '__main__':
    unittest.main()
