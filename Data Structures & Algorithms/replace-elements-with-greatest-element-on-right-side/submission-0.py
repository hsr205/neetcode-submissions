class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        left_pointer:int = 0
        right_pointer:int = len(arr)
        
        while left_pointer < right_pointer:
            
            window_list:list[int] = arr[left_pointer + 1:right_pointer]

            if not window_list:
                break

            max_value:int = max(window_list)

            arr[left_pointer] = max_value

            left_pointer += 1


        arr[left_pointer] = -1


        return arr
        