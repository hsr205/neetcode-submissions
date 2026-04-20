class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string_length_1:int = len(s)
        string_length_2:int = len(t)

        if string_length_1 != string_length_2:
            return False

        dict_obj_1:dict[str, int] = {}
        
        dict_obj_2:dict[str, int] = {}

        for character in s:

            if dict_obj_1.get(character) == None:
                dict_obj_1[character] = 1
            else:
                dict_obj_1[character] += 1

        for character in t:

            if dict_obj_2.get(character) == None:
                dict_obj_2[character] = 1
            else:
                dict_obj_2[character] += 1


        for character, char_frequency in dict_obj_1.items():
            if dict_obj_2.get(character) == None:
                return False
            else:
                if char_frequency != dict_obj_2.get(character):
                    return False


        return True
        