class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        num_frequency_dict:dict[int,int] = {}

        for num in nums:
            if num not in num_frequency_dict:
                num_frequency_dict[num] = 1
            elif num in num_frequency_dict:
                num_frequency_dict[num] += 1

        for index, (key, value) in enumerate(num_frequency_dict.items()):
            nums[index] = key

        return len(num_frequency_dict.values())