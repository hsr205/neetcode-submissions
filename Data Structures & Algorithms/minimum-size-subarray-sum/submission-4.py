class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        for element in nums:
            if element >= target:
                return 1

        pointer_1:int = 0
        pointer_2:int = 1
        value_accumulator:int = 0
        min_subarray_length:int = math.inf

        while pointer_1 < len(nums) - 1:

            if value_accumulator == 0:
                value_accumulator += nums[pointer_1] + nums[pointer_2]

            elif value_accumulator > 0:
                value_accumulator += nums[pointer_2]

            if value_accumulator >= target:
                min_subarray_length = min(min_subarray_length, (pointer_2 - pointer_1) + 1)
                pointer_1 += 1
                pointer_2 = pointer_1
                value_accumulator = 0

            pointer_2 += 1

            if pointer_2 >= len(nums):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1
                value_accumulator = 0

        if min_subarray_length == math.inf:
            return 0
                
        return min_subarray_length
        