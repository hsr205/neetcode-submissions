class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        for element in nums:
            if element >= target:
                return 1

        start_pointer:int = 0
        end_pointer:int = 1
        min_subarray_len:int = math.inf
        running_sum:int = nums[start_pointer]

        while end_pointer <= len(nums) - 1:

            running_sum += nums[end_pointer]

            while running_sum >= target:
                min_subarray_len = min(min_subarray_len, (end_pointer - start_pointer) + 1)
                running_sum -= nums[start_pointer]
                start_pointer += 1
            
            end_pointer += 1
    
        if min_subarray_len == math.inf:
            return 0

        return min_subarray_len
        