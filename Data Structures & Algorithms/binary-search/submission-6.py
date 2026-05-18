class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_pointer:int = 0
        right_pointer:int = len(nums) - 1

        while left_pointer <= right_pointer:

            middle_pointer:int = (left_pointer + right_pointer) // 2

            middle_value:int = nums[middle_pointer]

            if middle_value == target:
                return middle_pointer

            if middle_value < target:
                left_pointer = middle_pointer + 1

            if middle_value > target:
                right_pointer = middle_pointer - 1


        return -1
        