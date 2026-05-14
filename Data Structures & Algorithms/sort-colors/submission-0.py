class Solution:
    def sortColors(self, nums: List[int]) -> None:


        pointer_1:int = 0
        pointer_2:int = 1

        nums_length:int = len(nums) - 1

        while pointer_1 < nums_length:

            num_1:int = nums[pointer_1]
            num_2:int = nums[pointer_2]

            if num_1 > num_2:
                temp_num:int = num_1
                nums[pointer_1] = num_2
                nums[pointer_2] = temp_num


            pointer_2 += 1

            if pointer_2 >= len(nums):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1
        

        

        