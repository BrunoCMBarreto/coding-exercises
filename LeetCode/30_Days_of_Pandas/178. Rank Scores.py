# 178. Rank Scores
# Solved
# Medium
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Scores

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | score       | decimal |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 

# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores.score.rank(method="dense", ascending=False)
    return scores.sort_values(by="score", ascending=False).loc[:,["score","rank"]]

# Claude Response:

# import pandas as pd

# def rank_scores(scores: pd.DataFrame) -> pd.DataFrame:
#     # Create 'rank' column using dense_rank method
#     scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
#     # Sort by score in descending order
#     result = scores.sort_values(by='score', ascending=False)[['score', 'rank']]
    
#     return result