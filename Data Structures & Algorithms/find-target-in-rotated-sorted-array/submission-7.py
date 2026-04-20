class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums or len(nums) == 1 and nums[0] == target or len(nums) == 2 and nums[0] == target:
            return 0

        if len(nums) == 2 and nums[1] == target:
            return 1

        left_pointer:int = 0
        right_pointer:int = len(nums) - 1

        while left_pointer < right_pointer:

            middle_pointer:int = (right_pointer + left_pointer) // 2

            left_value:int = nums[left_pointer]
            middle_value:int = nums[middle_pointer]
            right_value:int = nums[right_pointer]

            if middle_value == target:
                return nums.index(middle_value)

            if nums[middle_pointer-1] == target:
                return nums.index(middle_value)-1

            if left_value == target:
                return nums.index(left_value)

            if right_value == target:
                return nums.index(right_value)

            if middle_value > left_value:
                left_pointer = middle_pointer
                middle_pointer += 1
                
            else:
                right_pointer = middle_pointer
                middle_pointer -= 1


        
        return -1
        