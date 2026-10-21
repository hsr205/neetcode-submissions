class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        result_list:list[int] = []

        left_pointer:int = 0
        right_pointer:int = len(numbers) - 1

        while left_pointer < right_pointer:

            left_value:int = numbers[left_pointer]
            right_value:int = numbers[right_pointer]
            sum_value:int = left_value + right_value

            if sum_value == target:
                return [left_pointer+1, right_pointer+1]

            elif sum_value > target:
                right_pointer -= 1
            
            elif sum_value < target:
                left_pointer += 1







        