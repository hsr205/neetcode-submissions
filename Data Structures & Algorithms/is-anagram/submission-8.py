class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_list:list[str] = list(sorted(s))
        t_list:list[str] = list(sorted(t))

        pointer_1:int = 0

        while pointer_1 < len(s_list):

            s_list_character:str = s_list[pointer_1]
            t_list_character:str = t_list[pointer_1]

            # print(f"s_list_character = {s_list_character}")
            # print(f"t_list_character = {t_list_character}")
            # print("")

            if s_list_character != t_list_character:
                return False

            pointer_1 += 1


        return True
        