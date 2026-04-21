class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k % len(nums) == 0:
            return

        nums.reverse()

        left_pointer:int = k % len(nums)
        right_pointer:int = len(nums) - 1
        
        while left_pointer < right_pointer:
            temp_value:int = nums[right_pointer]
            nums[right_pointer] = nums[left_pointer]
            nums[left_pointer] = temp_value
            left_pointer += 1
            right_pointer -= 1

        left_pointer = 0
        right_pointer = k % len(nums) - 1

        while left_pointer < right_pointer:
            temp_value:int = nums[right_pointer]
            nums[right_pointer] = nums[left_pointer]
            nums[left_pointer] = temp_value
            left_pointer += 1
            right_pointer -= 1

        
        