class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # set_length:int = len(set(nums))

        # if set_length < 3:
        #     return []

        # if set_length == 3:
        #     print("Inside conditional")
        #     return [nums]

        result_list:list[list[int]] = []

        pointer_1:int = 0
        pointer_2:int = 1
        pointer_3:int = 2


        while pointer_1 < pointer_2 and pointer_2 < pointer_3 and pointer_3 < len(nums):

            if nums[pointer_1] + nums[pointer_2] + nums[pointer_3] == 0 and pointer_1 != pointer_2 and pointer_2 != pointer_3:
                list_to_add:list[int] = sorted([nums[pointer_1],nums[pointer_2],nums[pointer_3]])

                if list_to_add not in result_list:
                    result_list.append(list_to_add)

            pointer_3 += 1

            if pointer_3 == len(nums):
                pointer_2 += 1
                pointer_3 = pointer_2 + 1
                if pointer_2 == len(nums) - 1:
                    pointer_1 += 1
                    pointer_2 = pointer_1 + 1
                    pointer_3 = pointer_2 + 1
                


        return result_list
        