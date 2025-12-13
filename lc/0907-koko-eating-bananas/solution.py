class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # output: integer k such that she can eat all bananas
        # k = 4
        # i = 0 -> eats all
        # i = 1 -> eats 4, 2 left from piles[1]
        # i = 2 -> eats 2 from piles[1], 2 from piles[2], 5 left
        # i = 3 -> eats 4 from piles[2], 1 left
        # i = 4 -> eats 1 from piles[2], 3 from piles[3], 4 left
        # i = 5
        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return high
