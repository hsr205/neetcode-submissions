class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result_list:list[int] = []

        pointer_1:int = 0
        pointer_2:int = 1

        while pointer_1 < len(nums) - 1:

            initial_value:int = nums[pointer_1]
            secondary_value:int = nums[pointer_2]

            sum_value:int = initial_value + secondary_value

            if sum_value == target:
                result_list.append(pointer_1)
                result_list.append(pointer_2)

            pointer_2 += 1

            if pointer_2 == len(nums):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1

        return result_list
        