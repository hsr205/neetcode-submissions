class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit:int = 0
        left_pointer:int = 0
        right_pointer:int = 1

        while right_pointer < len(prices):

            buy_price:int = prices[left_pointer]
            sell_price:int = prices[right_pointer]

            if buy_price < sell_price:
                max_profit = max(max_profit, abs(buy_price - sell_price))            
            else:
                left_pointer = right_pointer

            right_pointer += 1


        

        return max_profit
        