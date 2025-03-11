""" Moudle to handle the transactions for the vending machine.
"""
class TransactionManager:
    """ Class to handle the transactions for the vending machine
    """
    def __init__(self, supported_coins):
        """ Initialise and setup the coins.
        """
        self._supported_coins = sorted(supported_coins, reverse=True)

    def process_payment(self, total_amount, inserted_amount):
        """ Process the payment for the vending machine.

            Args:
                paid_amount (int): Amount paid for the product(s)
                total_amount (int): Total amount of coins inserted.
        """
        if inserted_amount < total_amount:
            raise ValueError("Insufficient funds")

        # Calculate the change and the coins required.
        change = inserted_amount - total_amount
        return self.__get_change(change)

    def __get_change(self, change):
        """ Calculate and return the change based on the available coin denominations.

            Args:
                change (int): Balance amount to be issued.
        """
        balance_coins = []

        # Calculate the number of coins based on the change/balance
        for coin in self._supported_coins:
            while change >= coin:
                change -= coin
                balance_coins.append(coin)

        return balance_coins
