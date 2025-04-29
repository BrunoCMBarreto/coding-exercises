# 176. Second Highest Salary
# Solved
# Medium
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 

# Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    N = 2
    if len(employee.salary.unique()) >= N & N > 0:
        nth_highest_value = employee.drop_duplicates(subset="salary").sort_values(by="salary", ascending=False).iloc[N-1,1]
    else:
        nth_highest_value = None
    return pd.DataFrame([nth_highest_value], columns=["SecondHighestSalary"])