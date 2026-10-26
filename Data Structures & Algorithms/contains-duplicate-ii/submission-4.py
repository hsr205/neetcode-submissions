class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        pointer_1:int = 0
        pointer_2:int = 1


        while pointer_1 < len(nums) - 1:

            if nums[pointer_1] == nums[pointer_2] and abs(pointer_1 - pointer_2) <= k:
                return True
        

            pointer_2 += 1

            if pointer_2 >= len(nums):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1


        return False
        