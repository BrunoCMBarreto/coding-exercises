# 1484. Group Sold Products By The Date
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table Activities:

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | sell_date   | date    |
# | product     | varchar |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each row of this table contains the product name and the date it was sold in a market.
 

# Write a solution to find for each date the number of different products sold and their names.

# The sold products names for each date should be sorted lexicographically.

# Return the result table ordered by sell_date.

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    product_series = activities.groupby("sell_date").product.unique().apply(sorted).apply(','.join).reset_index().rename(columns={"product":"products"})
    products_counted = activities.groupby("sell_date").nunique().rename(columns={"product":"num_sold"})
    activities_counted = pd.merge(products_counted, product_series, on="sell_date")
    return activities_counted
