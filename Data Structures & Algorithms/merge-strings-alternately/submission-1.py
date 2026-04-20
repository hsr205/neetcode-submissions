class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result_str:str = ""

        pointer_1:int = 0
        pointer_2:int = 0

        while pointer_1 < len(word1) and pointer_2 < len(word2):

            character_word_1:str = word1[pointer_1]
            character_word_2:str = word2[pointer_2]

            result_str += character_word_1 + character_word_2

            pointer_1 += 1
            pointer_2 += 1

        if word1[pointer_1:]:
            result_str += word1[pointer_1:]

        else:
            result_str += word2[pointer_2:]

        return result_str





        