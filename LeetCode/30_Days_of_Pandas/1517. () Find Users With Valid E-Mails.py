# 1517. Find Users With Valid E-Mails
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Users

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# | mail          | varchar |
# +---------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains information of the users signed up in a website. Some e-mails are invalid.
 

# Write a solution to find the users who have valid emails.

# A valid e-mail has a prefix name and a domain where:

# The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
# The domain is '@leetcode.com'.
# Return the result table in any order.

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    valid_chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.-01234567890")
    email_decomp_df = users.mail.str.rsplit(pat="@", n=1, expand=True)
    return users[(email_decomp_df.loc[:,0].str[0].isin(letters)) & 
                 (email_decomp_df.loc[:,0].apply(lambda string: all(char in valid_chars for char in string))) & 
                 (email_decomp_df.loc[:,1] == "leetcode.com")]

# Claude Solution:

# SELECT user_id, name, mail
# FROM Users
# WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$';

# ... This is not even python