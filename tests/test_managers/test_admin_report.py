""" Unit tests for admin report generation.
"""
import unittest
from unittest.mock import MagicMock

from core.managers.admin_report import AdminReport


class TestAdminReport(unittest.TestCase):
    """ Tests for admin report.
    """
    def setUp(self):
        """ Setting up the test data.
        """
        self.report = AdminReport(MagicMock(), MagicMock())
        self.report.inventory_manager.get_inventory_report.return_value = {"Product": 10}
        self.report.sales_manager.total_sales = 100
        self.report.sales_manager.product_sales = {"Product": {"quantity": 50, "revenue": 75}}

    def test_generate_report(self):
        """ Test to generate the report
        """
        report = self.report.generate_report()

        self.assertIn("inventory", report)
        self.assertIn("product_sales", report)
        self.assertIn("total_sales", report)

if __name__ == '__main__':
    unittest.main()
