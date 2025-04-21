# 607. Sales Person
# Solved
# Easy
# Topics
# Companies
# Hint
# SQL Schema
# Pandas Schema
# Table: SalesPerson

# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | sales_id        | int     |
# | name            | varchar |
# | salary          | int     |
# | commission_rate | int     |
# | hire_date       | date    |
# +-----------------+---------+
# sales_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.
 

# Table: Company

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | com_id      | int     |
# | name        | varchar |
# | city        | varchar |
# +-------------+---------+
# com_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name and the ID of a company and the city in which the company is located.
 

# Table: Orders

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | order_id    | int  |
# | order_date  | date |
# | com_id      | int  |
# | sales_id    | int  |
# | amount      | int  |
# +-------------+------+
# order_id is the primary key (column with unique values) for this table.
# com_id is a foreign key (reference column) to com_id from the Company table.
# sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
# Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.
 

# Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".

# Return the result table in any order.

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    sales_data = pd.merge(pd.merge(orders, company.rename(columns={"name":"company_name"}), on="com_id"), sales_person, how="outer", on="sales_id")
    return sales_data[~sales_data.name.isin(sales_data[sales_data.company_name == "RED"].name)][["name"]].drop_duplicates(subset="name")

# Claude Response:

# import pandas as pd

# def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     # Find the company ID for "RED"
#     red_com_id = company[company['name'] == 'RED']['com_id'].iloc[0]
    
#     # Find all sales IDs who have orders with "RED"
#     sales_with_red_orders = orders[orders['com_id'] == red_com_id]['sales_id'].unique()
    
#     # Find all salespersons who don't have orders with "RED"
#     result = sales_person[~sales_person['sales_id'].isin(sales_with_red_orders)]
    
#     # Return only the names column
#     return result[['name']]

# A much more pythonic way of approaching the problem that doesn't feel the need to join frames together