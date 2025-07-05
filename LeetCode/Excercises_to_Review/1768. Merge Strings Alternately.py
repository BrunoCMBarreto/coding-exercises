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