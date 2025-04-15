# 283. Move Zeroes
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_indices = []
        for ind, value in enumerate(nums):
            if value == 0:
                zero_indices.append(ind)
        for iter_ind, zero_ind in enumerate(zero_indices):
            nums.append(nums.pop(zero_ind-iter_ind))

# Clause Response:

# def moveZeroes(nums: list[int]) -> None:
#     # Position where we will place the next non-zero element
#     non_zero_pos = 0
    
#     # First pass: move all non-zero elements to the front
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[non_zero_pos] = nums[i]
#             non_zero_pos += 1
    
#     # Second pass: fill the remaining positions with zeros
#     for i in range(non_zero_pos, len(nums)):
#         nums[i] = 0
#
# Runs slower on lists that are not an overwhelming majority zeros