# 1693. Daily Leads and Partners
# Solved
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: DailySales

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | date_id     | date    |
# | make_name   | varchar |
# | lead_id     | int     |
# | partner_id  | int     |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
# The name consists of only lowercase English letters.
 

# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.

# Return the result table in any order.

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    grouped_sales = daily_sales.groupby(["date_id","make_name"]).agg({"lead_id":"nunique","partner_id":"nunique"}).reset_index().rename(columns={"lead_id":"unique_leads","partner_id":"unique_partners"})
    return grouped_sales[["date_id","make_name","unique_leads","unique_partners"]]

# Claude Response:

# import pandas as pd

# def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
#     # Group by date_id and make_name, then count distinct lead_id and partner_id
#     result = daily_sales.groupby(['date_id', 'make_name']).agg({
#         'lead_id': 'nunique',
#         'partner_id': 'nunique'
#     }).reset_index()
    
#     # Rename columns to match expected output
#     result.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']
    
#     return result