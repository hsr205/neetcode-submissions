class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # for index, value in enumerate(nums2):
        #     nums1[index] = value

        pointer_1:int = 0

        for index in range(m, len(nums1)):
            nums1[index] = nums2[pointer_1]

            pointer_1 += 1


        nums1.sort()

        
            






