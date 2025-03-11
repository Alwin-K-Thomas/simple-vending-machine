""" Unit tests for Product
"""
import unittest

from core.models.product import Product


class TestProduct(unittest.TestCase):
    """ Tests for defining a product.
    """
    def setUp(self):
        """ Setup a mock product.
        """
        self.product = Product("product1", 10, 100)

    def test_update_stock(self):
        """ Test to confirm that we can update the stock
            for a given product.
        """
        self.product.update_stock(-10)

        self.assertEqual(self.product.stock, 90)
        with self.assertRaises(ValueError):
            self.product.update_stock(-200)

if __name__ == "__main__":
    unittest.main()
