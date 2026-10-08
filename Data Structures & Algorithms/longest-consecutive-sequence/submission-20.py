class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_value:int = 0
        nums_set:set[int] = set(nums)

        for num in nums:

            longest_sequence_int:int = 0

            if (num - 1) not in nums_set:
                
                while (num + longest_sequence_int) in nums_set:
                    longest_sequence_int += 1
            
            max_value = max(longest_sequence_int, max_value)

        return max_value
        