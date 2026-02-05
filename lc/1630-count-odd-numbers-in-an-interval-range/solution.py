class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # generate range
        # 3, 5 => 3, 4, 5 => 2 ; 2 + 1
        # 3, 4 => 3
        # high = low + (n- 1)2
        # high - low = 2(n-1)
        # (high - low) / 2 = n - 1
        # (high - low) / 2 + 1 = n
        return (high + 1) // 2 - (low // 2)
