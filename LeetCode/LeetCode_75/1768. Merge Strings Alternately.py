# 1768. Merge Strings Alternately
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        char_list = []
        ind = 0
        while ind/2 < len(word1) or ind/2 < len(word2):
            if ind % 2 == 0 and ind//2 < len(word1):
                char_list.append(word1[ind//2])
            elif ind % 2 == 1 and ind//2 < len(word2):
                char_list.append(word2[ind//2])
            ind = ind + 1
        return "".join(char_list)

# Claude Answer:
# def mergeAlternately(word1: str, word2: str) -> str:
#     """
#     Merge two strings by adding letters in alternating order, starting with word1.
#     If one string is longer, append remaining letters to the end of the result.
    
#     Args:
#         word1: First string
#         word2: Second string
        
#     Returns:
#         Merged string with letters in alternating order
#     """
#     merged = []
#     i, j = 0, 0
    
#     # Add letters alternately until we reach the end of either string
#     while i < len(word1) and j < len(word2):
#         merged.append(word1[i])
#         merged.append(word2[j])
#         i += 1
#         j += 1
    
#     # Append remaining letters from word1 if any
#     merged.append(word1[i:])
    
#     # Append remaining letters from word2 if any
#     merged.append(word2[j:])
    
#     # Join all characters into a single string
#     return ''.join(merged)