class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # one pass: find min price and update max_profit
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            curr = prices[i]
            if curr > min_price:
                max_profit = max(max_profit, curr - min_price)
        
        return max_profit
