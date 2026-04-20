class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0 and len(nums2) > 0:

            for index in range(0, len(nums2)):
                nums1[index] = nums2[index]

            nums1.sort()

            return

        pointer_1:int = 0

        for index, element in enumerate(nums1):

            if element == 0:
                nums1[index] = nums2[pointer_1]
                pointer_1 += 1

            if pointer_1 > len(nums2) - 1:
                break

        nums1.sort()
        
        