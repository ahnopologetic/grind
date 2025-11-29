class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # O(n^2) -> for each price, find nearest smaller price and subtract it
        # optimal solution: ...?

        for i, price in enumerate(prices):
            j = i + 1
            while j < len(prices) and price < prices[j]:
                j += 1
            if j < len(prices):
                prices[i] = price - prices[j]
        
        return prices
