# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        h, t = 1, n
        first_bad_version = n

        while h <= t:
            m = (h + t) // 2
            if isBadVersion(m):
                first_bad_version = m
                t = m - 1
            else:
                h = m + 1
            
        
        return first_bad_version


