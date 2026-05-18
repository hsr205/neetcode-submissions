class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit:int = 0

        pointer_1:int = 0
        pointer_2:int = 1

        prices_list_length:int = len(prices) - 1

        while pointer_2 < len(prices):

            buy_price:int = prices[pointer_1]
            sell_price:int = prices[pointer_2]

            current_profit:int = sell_price - buy_price

            if current_profit > 0:
                max_profit += current_profit
            
            pointer_1 += 1
            pointer_2 += 1

        return max_profit

