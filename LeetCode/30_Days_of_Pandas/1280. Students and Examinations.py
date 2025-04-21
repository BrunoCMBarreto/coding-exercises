# 1280. Students and Examinations
# Solved
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Students

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# student_id is the primary key (column with unique values) for this table.
# Each row of this table contains the ID and the name of one student in the school.
 

# Table: Subjects

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | subject_name | varchar |
# +--------------+---------+
# subject_name is the primary key (column with unique values) for this table.
# Each row of this table contains the name of one subject in the school.
 

# Table: Examinations

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | subject_name | varchar |
# +--------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each student from the Students table takes every course from the Subjects table.
# Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
 

# Write a solution to find the number of times each student attended each exam.

# Return the result table ordered by student_id and subject_name.

import pandas as pd
from itertools import product

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_exams = examinations
    student_exams["count"] = 0
    student_exams["attended_exams"] = student_exams.groupby(["student_id","subject_name"]).transform("count")
    student_possible_exams = pd.DataFrame(product(students.student_id,subjects.subject_name), columns=["student_id", "subject_name"])
    student_exams = pd.merge(student_exams, student_possible_exams, how="outer", on=["student_id","subject_name"])
    student_exams = pd.merge(student_exams, students, how="left", on="student_id")
    student_exams = student_exams.fillna(value={"attended_exams":0})
    student_exams.sort_values(by=["student_id","subject_name"])
    return student_exams.drop_duplicates(subset=["student_id","subject_name"]).loc[:,["student_id","student_name","subject_name","attended_exams"]]

# Claude Response

# import pandas as pd

# def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
#     # Create a cartesian product of students and subjects
#     # This ensures all student-subject combinations are present
#     student_subject = students.merge(subjects, how='cross')
    
#     # Count exam attendances for each student and subject
#     exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    
#     # Merge the counts with the student-subject combinations
#     result = student_subject.merge(
#         exam_counts, 
#         on=['student_id', 'subject_name'], 
#         how='left'
#     ).fillna(0)
    
#     # Sort by student_id and subject_name as required
#     result = result.sort_values(['student_id', 'subject_name'])
    
#     # Ensure attended_exams is integer type
#     result['attended_exams'] = result['attended_exams'].astype(int)
    
#     # Select and order columns as per the expected output
#     result = result[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    
#     return result

# I was rather surprised to learn that pandas innately supports cartesian cross products in its merge method!