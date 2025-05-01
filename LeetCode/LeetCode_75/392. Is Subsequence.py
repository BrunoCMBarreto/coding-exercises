# 392. Is Subsequence
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequence_ind = 0
        if len(s) < 1:
            return True
        if len(s) > len(t):
            return False
        for char in t:
            if char == s[subsequence_ind]:
                subsequence_ind += 1
            if subsequence_ind >= len(s):
                return True
        return False
