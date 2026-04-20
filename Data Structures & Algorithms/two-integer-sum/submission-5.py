class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pointer_1:int = 0
        pointer_2:int = 1
        nums_list_length:int = len(nums)

        while pointer_1 != nums_list_length:

            starting_int:int = nums[pointer_1]
            subsequent_int:int = nums[pointer_2]
            result_int:int = starting_int + subsequent_int


            if result_int == target:
                result_list:list[int] = [pointer_1, pointer_2]
                return result_list

            pointer_2 += 1

            if pointer_2 == nums_list_length:
                pointer_1 += 1
                pointer_2 = pointer_1 + 1

        
        return []
        