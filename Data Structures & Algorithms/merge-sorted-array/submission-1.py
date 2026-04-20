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


        # if m == 0 and n > 0:
        #     nums1 = nums2
        #     return

        # if n == 0 and m > 0:
        #     return

        
        # pointer_1:int = 0
        # pointer_2:int = 0

        # back_counter:int = 1

        # while pointer_1 < len(nums1) or pointer_2 < len(nums2):
            
        #     if pointer_1 > m - 1:
        #         break
        #     if pointer_2 > n - 1:
        #         break

        #     num_1_element:int = nums1[pointer_1]
        #     num_2_element:int = nums2[pointer_2]

        #     if num_2_element < num_1_element:
        #         temp_value:int = nums1[pointer_1]
        #         nums1[pointer_1] = nums2[pointer_2]
        #         nums1[-back_counter] = temp_value
        #         back_counter -= 1


        #     pointer_1 += 1
        #     pointer_2 += 1

        # print(f"pointer_1 = {pointer_1}")
        # print(f"pointer_2 = {pointer_2}")

        # print(f"nums1 = {nums1}")
        # print(f"nums2 = {nums2}")

        # nums1.sort()
        
        