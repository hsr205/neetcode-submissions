class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left_pointer:int = 0
        right_pointer:int = 1

        max_profit:int = 0


        while right_pointer < len(prices):

            if prices[left_pointer] < prices[right_pointer]:

                max_profit = max(max_profit, abs(prices[left_pointer] - prices[right_pointer]))
                right_pointer += 1

            else:
                left_pointer = right_pointer
                right_pointer += 1

        return max_profit
        