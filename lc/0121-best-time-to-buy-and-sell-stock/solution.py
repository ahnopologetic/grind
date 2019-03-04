class Solution:
    cache = []
    def maxProfit(self, prices: List[int]) -> int:
        self.cache.clear()
        if len(prices) == 0:
            return 0
        for i, v in enumerate(prices):
            if v < max(prices[i:]):
                profit = max(prices[i:]) - v
                if profit not in self.cache: 
                    self.cache.append(profit)
        if len(self.cache) == 0:
            return 0
        print(self.cache)
        return sorted(self.cache, reverse=True)[0]
            
