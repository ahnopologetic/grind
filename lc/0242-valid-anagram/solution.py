from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tokens = defaultdict(int)
        for ch in s:
            tokens[ch] += 1
        
        for ch in t:
            if ch not in tokens:
                return False
            tokens[ch] -= 1
            if tokens[ch] == 0:
                del tokens[ch]
        
        return not tokens
