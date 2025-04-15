# 1873. Calculate Special Bonus
# Solved
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Employees

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
 

# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:,"bonus"] = employees.loc[:,"salary"]
    employees.loc[(employees.employee_id % 2 == 0) | (employees.name.str[0] == "M"), "bonus"] *= 0
    return employees.loc[:,["employee_id","bonus"]].sort_values(by="employee_id")

# Claude Response:


import pandas as pd

# def calculate_bonus(employees: pd.DataFrame) -> pd.DataFrame:
#     # Create a new dataframe with just employee_id
#     result = pd.DataFrame({'employee_id': employees['employee_id']})
    
#     # Calculate bonus using vectorized operations
#     # Condition 1: employee_id is odd
#     odd_id = employees['employee_id'] % 2 == 1
    
#     # Condition 2: name doesn't start with 'M'
#     not_m_name = ~employees['name'].str.startswith('M')
    
#     # Calculate bonus - where both conditions are true, set bonus to salary, otherwise 0
#     result['bonus'] = 0  # Default to 0
#     result.loc[odd_id & not_m_name, 'bonus'] = employees.loc[odd_id & not_m_name, 'salary']
    
#     # Sort by employee_id
#     result = result.sort_values('employee_id')
    
#     return result