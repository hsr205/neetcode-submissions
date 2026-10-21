class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left_pointer:int = 0
        right_pointer:int = len(nums) - 1

        while left_pointer <= right_pointer:

            middle_pointer:int = (left_pointer + right_pointer) // 2

            if nums[middle_pointer] == target:
                return middle_pointer

            elif nums[middle_pointer] > target:
                right_pointer = middle_pointer - 1
            
            elif nums[middle_pointer] < target:
                left_pointer = middle_pointer + 1

        return left_pointer
        