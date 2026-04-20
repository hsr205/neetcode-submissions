class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result_list:list[list[int]] = []
        sorted_list:list[int] = sorted(nums)

        starting_pointer:int = 0
        left_pointer:int = 1
        right_pointer:int = len(nums) - 1

        while left_pointer <= right_pointer:
            
            num_1:int = sorted_list[starting_pointer]
            num_2:int = sorted_list[left_pointer]
            num_3:int = sorted_list[right_pointer]
            result_value:int = num_1 + num_2 + num_3

            if result_value == 0:
                sub_result_list:list[int] = [num_1, num_2, num_3]

                if sub_result_list not in result_list:
                    result_list.append(sub_result_list)

                left_pointer += 1

            elif result_value > 0:
                right_pointer -= 1

            elif result_value < 0:
                left_pointer += 1

            if left_pointer == right_pointer:
                starting_pointer += 1
                left_pointer = starting_pointer + 1
                right_pointer = len(nums) - 1

        return result_list
        