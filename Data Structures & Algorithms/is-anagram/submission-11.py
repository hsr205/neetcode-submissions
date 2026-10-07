class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if s == t:
            return True

        if len(s) != len(t):
            return False

        
        s_dict:dict[str,int] = self.get_str_dict(s)
        t_dict:dict[str,int] = self.get_str_dict(t)

        if len(s_dict) != len(t_dict):
            return False

        for character, frequency_int in s_dict.items():

            if t_dict.get(character, 0) == 0:
                return False

            if s_dict.get(character) != t_dict.get(character):
                return False

        return True


    def get_str_dict(self, input_str:str) -> dict[str, int]:

        result_dict:dict[str,int] = {}

        for character in input_str:
            if character not in result_dict:
                result_dict[character] = 1

            elif character in result_dict:
                result_dict[character] += 1

        return result_dict