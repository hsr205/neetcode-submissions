class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        if len(nums) == 2 and nums[0] > nums[-1]:
            return nums[-1]

        left_pointer:int = 0
        right_pointer:int = len(nums) - 1
        min_value:int = math.inf

        while left_pointer <= right_pointer:

            middle_pointer:int = (left_pointer + right_pointer) // 2

            min_value = min(min_value, nums[middle_pointer], nums[left_pointer], nums[right_pointer])

            if nums[middle_pointer] > nums[left_pointer]:
                left_pointer = middle_pointer + 1
            
            else:
                right_pointer = middle_pointer - 1

        return min_value