# 605. Can Place Flowers
# Solved
# Easy
# Topics
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num_plantable = 0
        for flower_plot in range(len(flowerbed)):
            can_plant = True
            if (flowerbed[flower_plot] == 1):
                can_plant = False
            elif ((flower_plot - 1) >= 0) and (flowerbed[flower_plot - 1] == 1):
                can_plant = False
            elif ((flower_plot + 1) < len(flowerbed)) and (flowerbed[flower_plot+1] == 1):
                can_plant = False
            else:
                flowerbed[flower_plot] = 1
            if can_plant:
                num_plantable = num_plantable + 1
        return num_plantable >= n

# Claude (weirdly redundant?) Solution:
#
# def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
#     """
#     Determine if n new flowers can be planted in the flowerbed without violating
#     the no-adjacent-flowers rule.
    
#     Args:
#         flowerbed: Array where 0 represents an empty plot and 1 represents a planted plot
#         n: Number of new flowers to plant
        
#     Returns:
#         True if n flowers can be planted without adjacency, False otherwise
#     """
#     # Edge case: if n is 0, we can always return True
#     if n == 0:
#         return True
        
#     length = len(flowerbed)
#     count = 0
#     i = 0
    
#     while i < length:
#         # Check if current plot is empty and its adjacent plots are also empty
#         if (flowerbed[i] == 0 and 
#             (i == 0 or flowerbed[i - 1] == 0) and 
#             (i == length - 1 or flowerbed[i + 1] == 0)):
            
#             # Plant a flower here
#             flowerbed[i] = 1
#             count += 1
            
#             # If we've planted enough flowers, return True
#             if count >= n:
#                 return True
        
#         i += 1
    
#     # If we couldn't plant enough flowers
#     return count >= n