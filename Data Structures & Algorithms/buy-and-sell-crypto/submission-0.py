class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit:int = 0


        pointer_1:int = 0
        pointer_2:int = 1
        array_size:int = len(prices)

        while pointer_2 < array_size:

            selling_price:int = prices[pointer_1] - prices[pointer_2]

            if selling_price < 0 and abs(selling_price) > max_profit:
                max_profit = abs(selling_price)

            pointer_2 += 1
            
            if pointer_2 == array_size:
                pointer_1 += 1
                pointer_2 = pointer_1 + 1


        return max_profit
        