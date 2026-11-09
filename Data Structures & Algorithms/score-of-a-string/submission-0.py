class Solution:
    def scoreOfString(self, s: str) -> int:

        pointer_1:int = 0
        pointer_2:int = 1
        running_total:int = 0

        while pointer_2 < len(s):
            
            
            running_total += abs(ord(s[pointer_2]) - ord(s[pointer_1]))

            pointer_1 += 1
            pointer_2 += 1


        return running_total
        