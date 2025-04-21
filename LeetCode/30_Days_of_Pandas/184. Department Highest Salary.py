# 184. Department Highest Salary
# Medium
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Employee

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | id           | int     |
# | name         | varchar |
# | salary       | int     |
# | departmentId | int     |
# +--------------+---------+
# id is the primary key (column with unique values) for this table.
# departmentId is a foreign key (reference columns) of the ID from the Department table.
# Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

# Table: Department

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
# Each row of this table indicates the ID of a department and its name.
 

# Write a solution to find employees who have the highest salary in each of the departments.

# Return the result table in any order.

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department_salaries = pd.merge(employee.rename(columns={"name":"Employee","salary":"Salary"}),
                                   department.rename(columns={"name":"Department","id":"departmentId"}),
                                   on="departmentId")
    max_by_department = department_salaries.groupby(by="Department", as_index=False).Salary.max()#.index
    max_indices = (department_salaries["Department"] + department_salaries["Salary"].astype(str)).isin(max_by_department["Department"] + max_by_department["Salary"].astype(str)) 
    return department_salaries.loc[max_indices].loc[:,["Department", "Employee","Salary"]]