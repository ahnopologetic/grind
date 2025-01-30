class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        max_count = 0
        for ch in s:
            while ch in longest:
                longest = longest[1:]
            
            longest += ch
            max_count = max(max_count, len(longest))
        return max_count



