class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pointer_1:int = 0
        pointer_2:int = 1
        numbers_list_length:int = len(numbers)

        while pointer_1 != numbers_list_length:

            initial_value:int = numbers[pointer_1]
            secondary_value:int = numbers[pointer_2]
            sum_value:int = initial_value + secondary_value

            if sum_value == target:
                return [pointer_1+1, pointer_2+1]

            pointer_2 += 1

            if pointer_2 == numbers_list_length:
                pointer_1 += 1
                pointer_2 = pointer_1 + 1

        
        return []
        