import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        result_list:list[int] = []
        result_dict:dict[int, float] = {}

        for element in nums:

            if element not in result_dict:
                result_dict[element] = 1.0
            else:
                result_dict[element] += 1.0


        for key, value in result_dict.items():
            
            if value > len(nums) / 3 :
                result_list.append(key)


        return result_list
        