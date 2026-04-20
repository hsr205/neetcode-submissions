class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for character in s:
            if character not in s_dict:
                s_dict[character] = 1
            else:
                s_dict[character] += 1

        for character in t:
            if character not in t_dict:
                t_dict[character] = 1
            else:
                t_dict[character] += 1

        for key, value in s_dict.items():
            if key not in t_dict:
                return False
            elif t_dict[key] != value:
                return False
        
        return True

        