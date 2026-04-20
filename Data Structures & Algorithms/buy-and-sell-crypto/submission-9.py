import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        max_profit:int = 0

        left_pointer:int = 0
        right_pointer:int = 1

        while right_pointer < len(prices):

            buy_day_value:int = prices[left_pointer]
            sell_day_value:int = prices[right_pointer]

            if buy_day_value < sell_day_value:
                
                max_profit = max(max_profit, sell_day_value-buy_day_value)
                
            else:

                left_pointer = right_pointer

            right_pointer += 1


        return max_profit
        