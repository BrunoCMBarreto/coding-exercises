# 1071. Greatest Common Divisor of Strings
# Solved
# Easy
# Topics
# Companies
# Hint
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small_str = min([str1, str2], key=len)
        best_divisor = ""
        for chunk_size in range(1,len(small_str)+1):
            divisor_candidate = small_str[:chunk_size]
            if (divisor_candidate * (len(str1)//len(divisor_candidate))) == str1 and (divisor_candidate * (len(str2)//len(divisor_candidate))) == str2:
                best_divisor = small_str[:chunk_size]
        return best_divisor
    
