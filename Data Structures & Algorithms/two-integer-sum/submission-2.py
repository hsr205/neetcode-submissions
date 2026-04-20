class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result_index_list:list[int] = []

        pointer_1:int = 0
        pointer_2:int = 1
        array_length:int = len(nums)

        while pointer_2 != array_length:

            if nums[pointer_1] + nums[pointer_2] == target and pointer_1 != pointer_2:
                result_index_list.append(pointer_1)
                result_index_list.append(pointer_2)
                return result_index_list
            
            pointer_2 += 1

            if pointer_2 == array_length:
                pointer_1 += 1
                pointer_2 = pointer_1 + 1


        return []
        