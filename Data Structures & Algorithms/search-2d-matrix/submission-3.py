class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        
        for row in matrix:

            left_pointer:int = 0
            right_pointer:int = len(row) - 1

            while left_pointer <= right_pointer:

                middle_pointer:int = (left_pointer + right_pointer) // 2

                middle_value:int = row[middle_pointer]

                if middle_value == target:
                    return True

                if middle_value > target:
                    right_pointer = middle_pointer - 1
                
                if middle_value < target:
                    left_pointer = middle_pointer + 1


        return False
        