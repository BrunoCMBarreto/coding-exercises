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

# Claude Response:

# def isSubsequence(s: str, t: str) -> bool:
#     """
#     Determine if string s is a subsequence of string t.
    
#     Args:
#         s: The string to check if it's a subsequence
#         t: The main string
        
#     Returns:
#         True if s is a subsequence of t, False otherwise
#     """
#     # Edge case: an empty string is always a subsequence
#     if not s:
#         return True
    
#     # Edge case: if s is longer than t, it cannot be a subsequence
#     if len(s) > len(t):
#         return False
    
#     # Two-pointer approach
#     i = 0  # pointer for string s
    
#     # Iterate through each character in t
#     for char in t:
#         # If the current characters match, move the pointer for s
#         if i < len(s) and s[i] == char:
#             i += 1
#             # If we've matched all characters in s, return True
#             if i == len(s):
#                 return True
    
#     # If we've gone through all of t and haven't matched all of s, return False
#     return False

# Nearly identical to my own approach.