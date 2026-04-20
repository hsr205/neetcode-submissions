class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 0 or len(nums) == 1:
            return nums

        pointer_1:int = 0
        pointer_2:int = 1

        while pointer_1 < len(nums) - 1:

            initial_value:int = nums[pointer_1]
            secondary_value:int = nums[pointer_2]

            if initial_value > secondary_value:
                temp_value:int = initial_value
                nums[pointer_1] = secondary_value
                nums[pointer_2] = temp_value

            pointer_2 += 1

            if pointer_2 == len(nums):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1

        return nums
        