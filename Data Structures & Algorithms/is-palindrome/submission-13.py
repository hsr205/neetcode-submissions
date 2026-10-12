class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == " " or len(s) == 1:
            return True

        joined_str:str = ""

        for character in s:
            if character.isalnum():
                joined_str += character.lower()

        if joined_str == " ":
            return True

        left_pointer:int = 0
        right_pointer:int = len(joined_str) - 1

        while left_pointer < right_pointer:

            left_char:str = joined_str[left_pointer]
            right_char:str = joined_str[right_pointer]

            if left_char != right_char:
                return False

            left_pointer += 1
            right_pointer -= 1

        return True
        