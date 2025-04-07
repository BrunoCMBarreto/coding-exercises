# 1431. Kids With the Greatest Number of Candies
# Solved
# Easy
# Topics
# Companies
# Hint
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most_candies = max(candies)
        return [candy_count + extraCandies >= most_candies for candy_count in candies]


# Claude Answer:
#
# def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
#     """
#     Determine which kids will have the greatest number of candies after being given extraCandies.
    
#     Args:
#         candies: List where candies[i] is the number of candies the ith kid has
#         extraCandies: Number of extra candies to give to each kid (one at a time)
        
#     Returns:
#         Boolean list where result[i] is True if the ith kid would have the most candies
#         after receiving extraCandies, otherwise False
#     """
#     # Find the maximum number of candies any kid currently has
#     max_candies = max(candies)
    
#     # For each kid, check if their candies + extraCandies will be >= max_candies
#     result = [candy + extraCandies >= max_candies for candy in candies]
    
#     return result