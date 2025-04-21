# 1050. Actors and Directors Who Cooperated At Least Three Times
# Solved
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: ActorDirector

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp is the primary key (column with unique values) for this table.
 

# Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

# Return the result table in any order.

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    times_cooperated = actor_director.groupby(by=["actor_id","director_id"]).count().reset_index()
    return times_cooperated[times_cooperated.timestamp >= 3].loc[:,["actor_id","director_id"]]

# Claude Response:

# import pandas as pd

# def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
#     # Group by actor_id and director_id pair and count occurrences
#     cooperation_counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    
#     # Filter pairs with at least 3 collaborations
#     result = cooperation_counts[cooperation_counts['count'] >= 3][['actor_id', 'director_id']]
    
#     return result