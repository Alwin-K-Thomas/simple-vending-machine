""" Unit tests for Transaction Manager
"""
import unittest

from core.managers.transaction_manager import TransactionManager


class TestTransactionManager(unittest.TestCase):
    """ Tests for transaction manager class.
    """
    def setUp(self):
        """ Setup the managers.
        """
        self.manager = TransactionManager([1, 2, 5, 10])

    def test_process_payment_success(self):
        """ Test to confirm that we can process a
            successful payment.
        """
        change = self.manager.process_payment(3, 5)

        self.assertEqual(change, [2])

    def test_process_payment_insufficient_funds(self):
        """ Test to confirm that we can't process any payment
            without funds.
        """
        with self.assertRaises(ValueError):
            self.manager.process_payment(5, 3)

if __name__ == '__main__':
    unittest.main()
