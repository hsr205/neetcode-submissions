class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        left_pointer:int = 0
        right_pointer:int = len(nums) - 1

        num_iterations:int = 0

        while left_pointer <= right_pointer:

            middle_pointer:int = (left_pointer + right_pointer) // 2

            middle_value:int = nums[middle_pointer]

            if middle_value == target:
                return middle_pointer

            elif middle_value < target:
                left_pointer = middle_pointer + 1
            
            elif middle_value > target:
                right_pointer = middle_pointer - 1


        return left_pointer
        