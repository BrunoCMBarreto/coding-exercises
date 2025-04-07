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
    
# Claude Answer:
# def gcdOfStrings(str1: str, str2: str) -> str:
#     """
#     Find the largest string that divides both str1 and str2.
    
#     Args:
#         str1: First string
#         str2: Second string
        
#     Returns:
#         The largest string that divides both input strings
#     """
#     # If concatenation in different orders doesn't match, no common divisor exists
#     if str1 + str2 != str2 + str1:
#         return ""
    
#     # Use the GCD algorithm to find the length of the largest common divisor
#     def gcd(a, b):
#         while b:
#             a, b = b, a % b
#         return a
    
#     # GCD of the lengths gives us the length of the largest common divisor
#     gcd_length = gcd(len(str1), len(str2))
    
#     # Return the first gcd_length characters of either string
#     return str1[:gcd_length]