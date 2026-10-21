# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        if guess(n) == 0:
            return n
    
        left_pointer:int = 0
        right_pointer:int = n

        while left_pointer <= right_pointer:

            middle_pointer:int = (left_pointer + right_pointer) // 2
            guess_result:int = guess(middle_pointer)

            if guess_result == 0:
                return middle_pointer

            elif guess_result == -1:
                right_pointer = middle_pointer - 1

            elif guess_result == 1:
                left_pointer = middle_pointer + 1

        return -1
        