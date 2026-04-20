class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict:dict[str,int] = {}
        t_dict:dict[str,int] = {}

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
            if key not in t_dict.keys():
                return False
            else:
                if s_dict[key] != t_dict[key]:
                    return False

        return True
        