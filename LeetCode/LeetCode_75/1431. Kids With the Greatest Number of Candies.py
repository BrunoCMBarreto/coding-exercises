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
