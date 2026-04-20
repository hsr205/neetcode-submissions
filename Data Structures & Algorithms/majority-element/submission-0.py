class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        result_int:int = 0
        integer_dict:dict[int, int] = {}

        for num in nums:
            if num not in integer_dict:
                integer_dict[num] = 1
            else:
                integer_dict[num] += 1

        
        max_value:int = max(integer_dict.values())

        for key, value in integer_dict.items():
            if value == max_value:
                result_int = key
                break

        return result_int
        