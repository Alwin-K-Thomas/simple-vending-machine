""" Unit test for config loader mechanism
"""
import os
import unittest
from unittest.mock import patch, mock_open

from core.config.config_loader import ConfigLoader


class TestConfigLoader(unittest.TestCase):
    """ Tests to load config
    """
    @patch("builtins.open", new_callable=mock_open, read_data='{"all_coins": [1, 2, 5, 10]}')
    @patch("os.path.dirname", return_value="mocked/directory")
    def test_load_config(self, mock_dirname, mock_file):
        """ Test to confirm that we can load the config file.
        """
        config = ConfigLoader.load_config()
        self.assertEqual(config, {"all_coins": [1, 2, 5, 10]})
        expected_path = os.path.join("mocked/directory", "config.json")
        mock_file.assert_called_once_with(expected_path, 'r')

if __name__ == '__main__':
    unittest.main()
