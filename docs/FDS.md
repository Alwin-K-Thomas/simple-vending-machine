# Functional Design Specification (FDS)

## Overview
This document describes the functional requirements and behavior of the Simple Vending Machine.

## Requirements
- **Input**: Coin insertion, product selection.
- **Processing**: Validate payment, check inventory, update sales.
- **Output**: Dispense product, return change.

## Key Elements
1. **MachineController**: Handles product purchases and transactions.
2. **InventoryManager**: Tracks the product stock and overall inventory.
3. **SalesManager**: Records sales data for each of the products.
4. **TransactionManager**: Manages payments and change.
5. **Admin Report**: Generates system reports.

## Error Handling
- **Insufficient Funds**: Rejects the transaction.
- **Insufficient Stock**: Prevents the purchase.
- **Unsupported Coins**: Rejects invalid currency.
