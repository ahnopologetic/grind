class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack
        # output: list of final prices
        # for each price, find nearest smaller or equal price from index i and subtract it
        # can we use prices[j] multiple times? yes
        # example = [1,4,1,1,2] -> [0, 3,0,1,2]
        i, j = 0, 1
        for n in range(len(prices) - 1):
            while j < len(prices) and prices[i] < prices[j]:
                j += 1
            prices[i] = prices[i] - prices[j] if j < len(prices) else prices[i]
            i = i + 1
            j = i + 1
        return prices
