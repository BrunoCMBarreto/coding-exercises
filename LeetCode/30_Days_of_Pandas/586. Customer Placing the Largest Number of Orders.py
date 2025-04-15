# 586. Customer Placing the Largest Number of Orders
# Easy
# Topics
# Companies
# Hint
# SQL Schema
# Pandas Schema
# Table: Orders

# +-----------------+----------+
# | Column Name     | Type     |
# +-----------------+----------+
# | order_number    | int      |
# | customer_number | int      |
# +-----------------+----------+
# order_number is the primary key (column with unique values) for this table.
# This table contains information about the order ID and the customer ID.
 

# Write a solution to find the customer_number for the customer who has placed the largest number of orders.

# The test cases are generated so that exactly one customer will have placed more orders than any other customer.

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(orders.groupby("customer_number", as_index=False).count().sort_values(by="order_number", ascending=False).customer_number.head(1))