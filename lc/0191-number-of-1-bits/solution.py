class Solution:
    def hammingWeight(self, n: int) -> int:
        # convert to binary -> count # of 1's
        return len([d for d in bin(n)[2:] if d == "1"])
