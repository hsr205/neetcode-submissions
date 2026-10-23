class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for list_obj in matrix:

            is_value_found:bool = self.is_target_in_list(input_list=list_obj, 
                                                         target_int=target)
            
            if is_value_found:
                return True


        return False

    
    def is_target_in_list(self, input_list:list[int], target_int:int) -> bool:


        left_pointer:int = 0
        right_pointer:int = len(input_list) - 1

        while left_pointer <= right_pointer:

            middle_pointer:int = (left_pointer + right_pointer) // 2

            if input_list[middle_pointer] == target_int:
                return True

            if input_list[middle_pointer] > target_int:
                right_pointer = middle_pointer - 1
            
            if input_list[middle_pointer] < target_int:
                left_pointer = middle_pointer + 1

        return False


        