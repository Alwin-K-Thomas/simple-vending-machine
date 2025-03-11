# System Architecture

## Overview
The Simple Vending Machine follows an object-oriented design with separate managers for inventory, sales, and transactions.

## High-Level Architecture
```plaintext
+------------------------+
|   Vending Machine CLI  |
+------------------------+
           |
           v
+--------------------------+
|    MachineController     |
+--------------------------+
    |          |         |
    v          v         v
+-----------+ +-----------+ +------------------+
| Inventory | | Sales     | | Transaction      |
| Manager   | | Manager   | | Manager          |
+-----------+ +-----------+ +------------------+
