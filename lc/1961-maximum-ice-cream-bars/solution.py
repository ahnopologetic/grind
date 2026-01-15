class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # BF: thinking about sorting and pick from the smallest until coins run out
        # DP: bottom up
        costs.sort()
        res = 0
        for cost in costs:
            if cost > coins:
                break
            else:
                res += 1
                coins -= cost
        return res
