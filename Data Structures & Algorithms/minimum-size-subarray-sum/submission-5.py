class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if target in nums:
            return 1

        start_pointer:int = 0
        end_pointer:int = 1
        min_subarray_len:int = math.inf

        while end_pointer <= len(nums):

            window_list:list[int] = nums[start_pointer:end_pointer]

            if sum(window_list) >= target:
                min_subarray_len = min(min_subarray_len, len(window_list))
                window_list.pop(0)
                start_pointer += 1
            else:
                end_pointer += 1
    
        if min_subarray_len == math.inf:
            return 0

        return min_subarray_len
        