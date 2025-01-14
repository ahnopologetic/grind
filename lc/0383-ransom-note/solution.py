from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tokens = defaultdict(int)

        for char in magazine:
            tokens[char] += 1
        
        for char in ransomNote:
            if char not in tokens:
                return False
            
            if not tokens[char]:
                return False

            tokens[char] -= 1

        return True


