class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        if len(s) == 1:
            return 1
        left = right = 0
        counter = Counter()

        while right < len(s):
            r = s[right]
            counter[r] += 1

            while counter[r] > 1:
                l = s[left]
                counter[l] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        
        return res
