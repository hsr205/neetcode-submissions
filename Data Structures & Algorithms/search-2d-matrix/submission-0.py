class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:

            left_pointer:int = 0
            right_pointer:int = len(row) - 1

            while left_pointer <= right_pointer:

                middle_pointer:int = (left_pointer + right_pointer) // 2

                current_value:int = row[middle_pointer]

                if current_value == target:
                    return True

                elif current_value < target:
                    left_pointer = middle_pointer + 1

                else:
                    right_pointer = middle_pointer - 1



        return False
        