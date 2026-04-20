class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if not s1 and s2:
            return False

        if s1 and not s2:
            return False

        if not s1 and not s2:
            return True

        if len(s1) > len(s2):
            return False

        s1_list:list[str] = sorted([x for x in s1])
        s2_list:list[str] = [x for x in s2]

        left_pointer:int = 0
        right_pointer_s1:int = len(s1_list)
        right_pointer_s2:int = len(s2_list) - 1

        while left_pointer <= right_pointer_s2:

            window_list = sorted(s2_list[left_pointer:right_pointer_s1])

            if window_list == s1_list:
                return True 

            left_pointer += 1
            right_pointer_s1 += 1

        return False
        