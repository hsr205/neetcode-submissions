class Solution:
    def findMin(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]


        min_value:int = 1001

        left_pointer:int = 0
        right_pointer:int = len(nums) - 1

        counter:int = 0

        while left_pointer < right_pointer:
            
            middle_pointer:int = (right_pointer + left_pointer) // 2

            left_value:int = nums[left_pointer]
            middle_value:int = nums[middle_pointer]
            right_value:int = nums[right_pointer]

            # print(f"left_pointer = {left_pointer}")
            # print(f"right_pointer = {right_pointer}")

            # print("")

            # print(f"left_value = {left_value}")
            # print(f"middle_value = {middle_value}")
            # print(f"right_value = {right_value}")

            min_value = min(min_value, middle_value)

            # print(f"min_value = {min_value}")

            # print("")


            if middle_value > left_value:
                min_value = min(min_value, left_value)
                left_pointer = middle_pointer
                middle_pointer += 1
            else:
                min_value = min(min_value, right_value)
                right_pointer = middle_pointer
                middle_pointer -= 1

            # if counter == 10:
            #     break

            # counter += 1

        return min_value
        