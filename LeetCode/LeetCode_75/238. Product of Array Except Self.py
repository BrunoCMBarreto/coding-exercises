# 238. Product of Array Except Self
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time.

import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = math.prod(nums)
        return [total_product//nums[ind] if nums[ind] != 0 else math.prod(nums[:ind] + nums[ind+1:]) for ind in range(len(nums))]
