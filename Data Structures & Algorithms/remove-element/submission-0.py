class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        index_list:list[int] = [index for index, num in enumerate(nums) if val == num]

        for index_num in index_list[::-1]:
            del nums[index_num]

        return len(nums)
        