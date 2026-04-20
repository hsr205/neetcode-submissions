class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pointer_1:int = 0
        pointer_2:int = 1

        while pointer_1 <= len(numbers) - 1:

            if numbers[pointer_1] + numbers[pointer_2] == target:
                return [pointer_1+1, pointer_2+1]

            pointer_2 += 1

            if pointer_2 == len(numbers):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1

        return []
        