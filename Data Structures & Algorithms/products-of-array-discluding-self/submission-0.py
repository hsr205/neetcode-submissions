import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result_list:list[int] = []

        for index in range(0, len(nums)):
            
            initial_list:list[int] = nums[:index]
            secondary_list:list[int] = nums[index+1:]


            product_value_1:int = math.prod(initial_list)
            product_value_2:int = math.prod(secondary_list)

            result_value:int = product_value_1 * product_value_2

            result_list.append(result_value)


        return result_list
        