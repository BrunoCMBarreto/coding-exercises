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