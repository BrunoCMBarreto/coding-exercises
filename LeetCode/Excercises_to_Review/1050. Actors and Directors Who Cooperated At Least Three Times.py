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
