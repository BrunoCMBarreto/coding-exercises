# 345. Reverse Vowels of a String
# Easy
# Topics
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]

        string_vowels_reversed = [letter for letter in s if letter.lower() in vowels]
        string_vowels_reversed.reverse()
        vowel_indices = [ind for ind, letter in enumerate(s) if letter.lower() in vowels]
        reverse_vowel_mapping = dict(zip(vowel_indices, string_vowels_reversed))
        return "".join([letter if ind not in vowel_indices else reverse_vowel_mapping[ind] for ind, letter in enumerate(s)])
    
# Alternatively:

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]
        string_vowels_reversed = []
        vowel_indices = []
        string_list = list(s)

        for ind, letter in enumerate(string_list):
            if letter.lower() in vowels:
                string_vowels_reversed.append(letter)
                vowel_indices.append(ind)
        string_vowels_reversed.reverse()

        for ind, vowel_ind in enumerate(vowel_indices):
            string_list[vowel_ind] = string_vowels_reversed[ind]

        return "".join(string_list)

# Claude Solution:
#
# def reverseVowels(s: str) -> str:
#     """
#     Reverse only the vowels in a string.
    
#     Args:
#         s: Input string
        
#     Returns:
#         String with vowels reversed
#     """
#     # Convert string to list since strings are immutable in Python
#     chars = list(s)
    
#     # Define vowels (both lowercase and uppercase)
#     vowels = set('aeiouAEIOU')
    
#     # Use two pointers approach
#     left, right = 0, len(s) - 1
    
#     while left < right:
#         # Find vowel from left
#         while left < right and chars[left] not in vowels:
#             left += 1
        
#         # Find vowel from right
#         while left < right and chars[right] not in vowels:
#             right -= 1
        
#         # Swap the vowels
#         chars[left], chars[right] = chars[right], chars[left]
        
#         # Move pointers
#         left += 1
#         right -= 1
    
#     # Convert list back to string
#     return ''.join(chars)