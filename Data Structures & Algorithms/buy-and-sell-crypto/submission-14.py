class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit:int = 0

        pointer_1:int = 0
        pointer_2:int = 1

        max_profit_list:list[int] = []
        price_list_length:int = len(prices) - 1

        while pointer_1 < price_list_length:

            buy_value:int = prices[pointer_1]
            sell_value:int = prices[pointer_2]

            current_profit:int = sell_value - buy_value

            if current_profit > 0:
                max_profit_list.append(current_profit)

            if len(max_profit_list) >= 1 and max(max_profit_list) > max_profit:
                max_profit = max(max_profit_list)

            pointer_2 += 1

            if pointer_2 > price_list_length:
                pointer_1 += 1
                pointer_2 = pointer_1 + 1
                max_profit_list = []


        return max_profit
        