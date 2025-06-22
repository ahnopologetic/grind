class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = result = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen: # TODO
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            result = max(result, right - left + 1)
        
        return result
