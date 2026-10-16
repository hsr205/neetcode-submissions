class Solution:
    def isPalindrome(self, s: str) -> bool:

        result_str:str = ""

        for character in s:

            if character.isalnum():
                result_str += character.lower()

        return result_str == result_str[::-1]
        