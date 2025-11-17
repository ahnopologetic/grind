class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        res, val = 0, abs(x)
        while val:
            val, mod = divmod(val, 10)
            res = res * 10 + mod
            if res > 2**31 - 1:
                return 0
        return sign * res
