# 2877. Create a DataFrame from List

# Write a solution to create a DataFrame from a 2D list called student_data.
# This 2D list contains the IDs and ages of some students.

# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.


import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])


# Claude answer for comparison:

# Import pandas as pd
# from typing import List

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     """
#     Create a DataFrame from a 2D list of student data.
    
#     Args:
#         student_data (List[List[int]]): A 2D list where each inner list contains
#                                          [student_id, age]
    
#     Returns:
#         pd.DataFrame: A DataFrame with columns 'student_id' and 'age'
#     """
#     # Create the DataFrame with the provided column names
#     df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    
#     return df