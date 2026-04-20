import math

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_pointer:int = 0
        right_pointer:int = len(heights) - 1

        max_value:int = -math.inf

        while left_pointer < right_pointer:


            initial_value:int = heights[left_pointer]
            secondary_value:int = heights[right_pointer]

            height_value:int = min(initial_value, secondary_value) 
            width_value:int = right_pointer - left_pointer
            area_value:int = height_value * width_value

            max_value:int = max(max_value, area_value)

            if initial_value < secondary_value:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_value
        