class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result_dict = {}

        for num in nums:
            if num in result_dict:
                return True
            else:
                result_dict[num] = 1

        
        return False
