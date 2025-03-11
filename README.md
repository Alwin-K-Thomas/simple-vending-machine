# Simple Vending Machine

[![codecov](https://codecov.io/gh/Alwin-K-Thomas/simple-vending-machine/branch/main/graph/badge.svg?token=GNB1EK2CHC)](https://codecov.io/gh/Alwin-K-Thomas/simple-vending-machine)
![CI](https://github.com/Alwin-K-Thomas/simple-vending-machine/actions/workflows/ci.yml/badge.svg)

This is a simple vending machine system implemented in Python. This system allows users to purchase products, manage inventory, track sales, and handle transactions with coin-based payments. 

It follows a modular architecture with separate managers for inventory, sales, transactions, and reporting. 

---

## **Features**
- Insert coins and purchase products.
- Maintain inventory stock.
- Sales and revenue tracking.
- Admin reporting for stock and sales.
- Unit tests with high test coverage.

## Additional Documentation
- [System Architecture](docs/ARCHITECTURE.md)
- [Functional Design Specification (FDS)](docs/FDS.md)
- [User Stories](docs/USER_STORIES.md)

## How to Run

1.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `main.py`).
2.  **Navigate to the Directory:** Open your terminal or command prompt and navigate to the directory where you saved the file.
3.  **Run the Script:** Execute the script using the following command:

    ```bash
    python main.py
    ```

## Usage
Once the script is running, you will see the main menu with the following options:

```text
Options:
1. Insert Coins
2. Purchase Product
3. View Admin Report
4. Exit
```
### 1. Insert Coins

-   Enter `1` to insert coins.
-   You will be prompted to enter the coin value. Accepted coin values are 1, 2, 5, and 10.
-   Enter `0` to stop inserting coins.
-   The total inserted amount will be displayed after each coin insertion.
-   Invalid coin values will prompt an error message.

### 2. Purchase Product

-   Enter `2` to purchase a product.
-   The available products with their prices and stock will be displayed.
-   Your current balance will also be shown.
-   Enter the name of the product you want to purchase.
-   Enter the quantity you want to purchase.
-   If you have sufficient balance, the purchase will be processed.
-   You will receive a success message, the amount of change returned (if any), and your remaining balance.
-   If you have insufficient balance or enter an invalid product name or quantity, an error message will be displayed.
-   After a successful purchase the inserted coins are reset to 0.

### 3. View Admin Report

-   Enter `3` to view the admin report.
-   The report will display the current inventory and sales information.

### 4. Exit

-   Enter `4` to exit the application.
-   A "Thank you!" message will be displayed.
