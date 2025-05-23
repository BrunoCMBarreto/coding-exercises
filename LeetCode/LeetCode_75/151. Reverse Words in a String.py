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
