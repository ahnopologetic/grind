class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        words = [0] * 26
        for ch in s:
            words[ord(ch) - ord('a')] += 1
        
        for ch in t:
            n = ord(ch) - ord('a')
            if words[n] <= 0:
                return False
            words[n] -= 1
        
        return True
