# 443. String Compression
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

class Solution:
    def compress(self, chars: List[str]) -> int:
        ind = 0
        consecutive_chars = []
        char_counts = []
        for char in chars:
            if (consecutive_chars or [None])[-1] != char:
                consecutive_chars.append(char)
                char_counts.append(1)
            else:
                char_counts[-1] = char_counts[-1] + 1
        
        chars.clear()
        for char, count in zip(consecutive_chars, char_counts):
            chars.append(char)
            if count > 1:
                for num_char in str(count):
                    chars.append(num_char)
        return len(chars)

# Claude Response:

# def compress(chars: list[str]) -> int:
#     if not chars:
#         return 0
        
#     write_index = 0  # Position where we write the compressed result
#     count = 1        # Count of current character
    
#     for read_index in range(1, len(chars) + 1):
#         # When we reach the end of array or a different character
#         if read_index == len(chars) or chars[read_index] != chars[read_index - 1]:
#             # Write the character
#             chars[write_index] = chars[read_index - 1]
#             write_index += 1
            
#             # If count > 1, write the count digits
#             if count > 1:
#                 # Convert count to string and write each digit
#                 count_str = str(count)
#                 for digit in count_str:
#                     chars[write_index] = digit
#                     write_index += 1
            
#             # Reset count for the next character
#             count = 1
#         else:
#             # Increment count for consecutive characters
#             count += 1
    
#     return write_index  # This is the new length
