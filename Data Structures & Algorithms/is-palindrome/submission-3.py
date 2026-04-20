class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        concatenated_str:str = ""

        for character in s:
            if character.isalnum():
                concatenated_str += character.lower()

        reversed_str:str = concatenated_str[::-1]

        return concatenated_str == reversed_str


        