# 1795. Rearrange Products Table
# Solved
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Products

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | store1      | int     |
# | store2      | int     |
# | store3      | int     |
# +-------------+---------+
# product_id is the primary key (column with unique values) for this table.
# Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
# If the product is not available in a store, the price will be null in that store's column.
 

# Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

# Return the result table in any order.

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
        return pd.melt(products,id_vars=['product_id'],value_vars=['store1','store2','store3'],var_name='store',value_name='price').dropna(subset=['price'])

# Claude Response:

# import pandas as pd

# def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
#     # Use melt to transform from wide to long format
#     result = pd.melt(
#         products,
#         id_vars=['product_id'],
#         value_vars=['store1', 'store2', 'store3'],
#         var_name='store',
#         value_name='price'
#     )
    
#     # Remove rows with null prices
#     result = result.dropna(subset=['price'])
    
#     # Clean up store names by removing the number (store1 -> store)
#     result['store'] = result['store'].str.replace('store', '')
    
#     return result

# ...
# This LLM response is odd, seeing as how it randomly concludes by stating that it should remove the number from the store column entries
# (which would completely defeat the point of having it), before proceeding to remove the word "store" instead (Which is more reasonable 
# but still completely unnecessary)