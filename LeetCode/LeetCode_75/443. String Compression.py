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
