# 334. Increasing Triplet Subsequence
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
# If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        doublet_ind = 0

        while doublet_ind < (len(nums) - 1):
            running_min = nums[doublet_ind]
            running_almost_min = nums[doublet_ind+1]
            if running_min < running_almost_min:
                 break
            if doublet_ind >= (len(nums) - 2):
                return False
            doublet_ind = doublet_ind + 1
        
        for ind, value in enumerate(nums[doublet_ind:]):
            if value > running_almost_min:
                return True
            elif running_almost_min > value > running_min:
                running_almost_min = value
            elif running_min > value and ind+1 < len(nums) and nums[ind+1] > value:
                if nums[ind+1] > running_almost_min:
                    return True
                running_min = value
                running_almost_min = nums[ind+1]
        return False


# Claude Response:

# def increasingTriplet(nums: list[int]) -> bool:
#     # Initialize first and second to the largest possible values
#     first = float('inf')  # smallest element seen so far
#     second = float('inf') # second smallest element seen so far
    
#     for num in nums:
#         # If current number is smaller than the smallest, update first
#         if num <= first:
#             first = num
#         # If current number is between first and second, update second
#         elif num <= second:
#             second = num
#         # If current number is greater than both first and second, we found a triplet
#         else:
#             return True
    
#     # If we've gone through the entire array without finding a triplet
#     return False

# ...Legitimately did not know you could simply instantiate an infinite value without numpy