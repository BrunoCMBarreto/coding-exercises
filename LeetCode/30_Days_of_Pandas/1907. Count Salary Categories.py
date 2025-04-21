# 1907. Count Salary Categories
# Solved
# Medium
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Accounts

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | account_id  | int  |
# | income      | int  |
# +-------------+------+
# account_id is the primary key (column with unique values) for this table.
# Each row contains information about the monthly income for one bank account.
 

# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.

# Return the result table in any order.

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"accounts_count":[(accounts.income < 20000).sum(), ((20000 <= accounts.income) & (accounts.income <= 50000)).sum(), (50000 < accounts.income).sum()],
                         "category":["Low Salary", "Average Salary", "High Salary"]})

# Claude Response:

# import pandas as pd

# def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
#     # Create a dataframe with all categories (to ensure all categories appear in result)
#     categories = pd.DataFrame({
#         'category': ['Low Salary', 'Average Salary', 'High Salary']
#     })
    
#     # Count accounts in each category
#     low_count = (accounts['income'] < 20000).sum()
#     avg_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
#     high_count = (accounts['income'] > 50000).sum()
    
#     # Create result dataframe
#     counts = pd.DataFrame({
#         'category': ['Low Salary', 'Average Salary', 'High Salary'],
#         'accounts_count': [low_count, avg_count, high_count]
#     })

# The categories df is completely unnecessary and unused for some reason, but the solution is good otherwise...
    