class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pointer_1:int = 0
        pointer_2:int = 1

        while pointer_1 <= len(nums) - 1:

            i_value:int = nums[pointer_1]
            j_value:int = nums[pointer_2]

            if i_value + j_value == target:
                return [pointer_1, pointer_2]

            pointer_2 += 1

            if pointer_2 == len(nums):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1

        return []
        