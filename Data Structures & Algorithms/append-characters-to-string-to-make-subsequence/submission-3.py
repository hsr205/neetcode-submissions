class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        pointer_1:int = 0
        pointer_2:int = 0

        while pointer_1 < len(s) and pointer_2 < len(t):

            s_char:str = s[pointer_1]
            t_char:str = t[pointer_2]


            if s_char == t_char:
                pointer_1 += 1
                pointer_2 += 1
            
            elif s_char != t_char:
                pointer_1 += 1


        if pointer_2 == len(t):
            return 0

        if pointer_2 == 0:
            return len(t)
        
    
        return len(t[pointer_2:])
        