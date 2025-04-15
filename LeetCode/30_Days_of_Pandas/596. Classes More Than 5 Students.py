# 596. Classes More Than 5 Students
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Courses

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# (student, class) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the name of a student and the class in which they are enrolled.
 

# Write a solution to find all the classes that have at least five students.

# Return the result table in any order.

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    course_student_counts = courses.groupby("class").count().reset_index()
    return pd.DataFrame(course_student_counts[course_student_counts.student >= 5].loc[:,"class"])