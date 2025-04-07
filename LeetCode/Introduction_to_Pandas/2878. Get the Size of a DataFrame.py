# 2878. Get the Size of a DataFrame
# Solved
# Easy
# Companies
# Hint
# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+
# Write a solution to calculate and display the number of rows and columns of players.

# Return the result as an array:

# [number of rows, number of columns]

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

# Claude Solution:
#
# import pandas as pd
# from typing import List

# def getDataframeSize(players: pd.DataFrame) -> List[int]:
#     """
#     Calculate the number of rows and columns in the DataFrame.
    
#     Args:
#         players (pd.DataFrame): Input DataFrame
    
#     Returns:
#         List[int]: A list containing [number of rows, number of columns]
#     """
#     # Use the shape attribute which returns a tuple of (rows, columns)
#     return list(players.shape)