# 1667. Fix Names in a Table
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Users

# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | name           | varchar |
# +----------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

# Return the result table ordered by user_id.

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users.name = users.name.str[0].str.upper() + users.name.str[1:].str.lower()
    return users.sort_values(by="user_id")