# 2885. Rename Columns
# Solved
# Easy
# Companies
# Hint
# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | id          | int    |
# | first       | object |
# | last        | object |
# | age         | int    |
# +-------------+--------+
# Write a solution to rename the columns as follows:

# id to student_id
# first to first_name
# last to last_name
# age to age_in_years

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ['student_id', 'first_name', 'last_name', 'age_in_years']
    return students