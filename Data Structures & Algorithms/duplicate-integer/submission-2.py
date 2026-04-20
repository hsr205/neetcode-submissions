class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        list_length:int = len(nums)

        set_length:int = len(set(nums))

        if list_length == set_length:
            return False
        else:
            return True
        