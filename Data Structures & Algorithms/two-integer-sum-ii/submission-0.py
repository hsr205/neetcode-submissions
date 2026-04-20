class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        result_list:list[int] = []


        pointer_1:int = 0
        pointer_2:int = 1
        array_size:int = len(numbers)

        while pointer_2 != array_size:

            if numbers[pointer_1] + numbers[pointer_2] == target and pointer_1 != pointer_2:
                result_list.append(pointer_1+1)
                result_list.append(pointer_2+1)
                return result_list

            pointer_2 += 1

            if pointer_2 == array_size:
                pointer_1 += 1
                pointer_2 = pointer_1 + 1


        return result_list
        