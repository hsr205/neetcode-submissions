# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left_value:int = 1
        right_value:int = n

        if guess(left_value) == 0:
            return left_value

        if guess(right_value) == 0:
            return right_value

        while True:

            middle_value:int = (left_value + right_value) // 2

            return_value:int = guess(middle_value)

            if return_value == 0:
                return middle_value

            if return_value == -1:
                right_value = middle_value

            if return_value == 1:
                left_value = middle_value


        return 0

        