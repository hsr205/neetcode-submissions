class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        character_dict_1:dict[str,int] = self.get_character_dict(s)
        character_dict_2:dict[str,int] = self.get_character_dict(t)

        for character, _ in character_dict_1.items():

            if character_dict_2.get(character, 0) == 0:
                return False
            
            elif character_dict_1.get(character) != character_dict_2.get(character, 0):
                return False

        return True

    def get_character_dict(self, input_str:str) -> dict[str, int]:

        result_dict:dict[str, int] = {}


        for character in input_str:

            if character not in result_dict:
                result_dict[character] = 1
            else:
                result_dict[character] += 1

        return result_dict
        