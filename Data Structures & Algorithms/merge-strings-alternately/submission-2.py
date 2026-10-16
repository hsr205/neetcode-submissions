class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result_str:str = ""

        pointer_1:int = 0
        pointer_2:int = 0


        while True:

            character_1:str = word1[pointer_1]
            character_2:str = word2[pointer_2]


            result_str += character_1
            result_str += character_2

            pointer_1 += 1
            pointer_2 += 1

            if pointer_1 >= len(word1):
                result_str += word2[pointer_2:]
                return result_str
            
            if pointer_2 >= len(word2):
                result_str += word1[pointer_1:]
                return result_str


        
        