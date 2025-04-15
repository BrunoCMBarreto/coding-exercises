# 151. Reverse Words in a String
# Solved
# Medium
# Topics
# Companies
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

# Claude Response:
#
# def reverseWords(s: str) -> str:
#     # Split the string into words and filter out empty strings
#     words = [word for word in s.split() if word]
    
#     # Reverse the array of words
#     words.reverse()  # or words = words[::-1]
    
#     # Join the words with a single space
#     return " ".join(words)
#
# Due to its use of a list comprehension, it fails the LeetCode tests that have excessively large inputs