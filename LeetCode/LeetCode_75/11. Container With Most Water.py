# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container_area = 0
        left_wall_ind = 0
        right_wall_ind = len(height) - 1
        current_width = len(height) - 1
        while current_width > 0:
            current_container_height = min(height[left_wall_ind], height[right_wall_ind])
            current_container_area = current_width * current_container_height
            if current_container_area > max_container_area:
                max_container_area = current_container_area
            if current_container_height == height[left_wall_ind]:
                left_wall_ind += 1
            else:
                right_wall_ind -= 1
            current_width -= 1
        return max_container_area


# OR

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container_area = 0
        current_max_container_height = 0
        for width in range(len(height)-1, 0, -1):
            for left_col_ind in range(len(height) - width):
                left_wall_height = height[left_col_ind]
                right_wall_height = height[left_col_ind + width]
                if left_wall_height > current_max_container_height and right_wall_height > current_max_container_height:
                    current_container_height = min(left_wall_height, right_wall_height)
                    current_area = width * current_container_height
                    if current_area > max_container_area:
                        max_container_area = current_area
                        current_max_container_height = current_container_height
        return max_container_area

# Claude Response:

# def maxArea(height: list[int]) -> int:
#     """
#     Find the maximum area of water that can be contained between two vertical lines.
    
#     Args:
#         height: List of heights representing vertical lines
        
#     Returns:
#         The maximum area of water that can be contained
#     """
#     left = 0
#     right = len(height) - 1
#     max_area = 0
    
#     while left < right:
#         # Calculate width between the two lines
#         width = right - left
        
#         # Calculate the area using the shorter line as height
#         area = width * min(height[left], height[right])
        
#         # Update the maximum area
#         max_area = max(max_area, area)
        
#         # Move the pointer of the shorter line inward
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
    
#     return max_area

# The same solution as my first listed solution