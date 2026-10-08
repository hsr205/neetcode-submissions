import math

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        max_length:int = 0
        current_length:int = 0
        nums_set:set[int] = set(nums)

        for num in nums_set:
            if (num - 1) not in nums_set:
                current_length = 0

                while (num + current_length) in nums_set:
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length
        