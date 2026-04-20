class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        max_profit:int = -1

        pointer_1:int = 0
        pointer_2:int = 1

        counter:int = 0

        while pointer_1 < len(prices) - 1:

            buy_price:int = prices[pointer_1]
            sell_price:int = prices[pointer_2]

            total_profit:int = sell_price - buy_price

            if total_profit > max_profit:
                max_profit = total_profit

            pointer_2 += 1

            if pointer_2 >= len(prices):
                pointer_1 += 1
                pointer_2 = pointer_1 + 1

        if max_profit == -1:
            return 0

        return max_profit
        