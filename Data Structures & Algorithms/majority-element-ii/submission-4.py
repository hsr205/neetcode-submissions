import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        
        if len(nums) == 1:
            return nums
        
        result_list:list[int] = []
        frequency_dict:dict[int,int] = {}

        for num in nums:
            
            if num not in frequency_dict:
                frequency_dict[num] = 1
        
            else:
                frequency_dict[num] += 1

        for key, value in frequency_dict.items():

            threshold_value_int:int = math.floor(len(nums) / 3)

            if value > threshold_value_int:
                result_list.append(key)


        return sorted(result_list)
        