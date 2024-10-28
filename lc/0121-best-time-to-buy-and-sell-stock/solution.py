class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 999999999
        max_profit = -9999999

        for _, price in enumerate(prices):
            min_price = min(min_price, price)
            if max_profit < price - min_price:
                max_profit = price - min_price
            
        
        return max_profit
