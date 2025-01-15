from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # store each char in hashmap
        # add char with even numbers (each / 2) + longest odd char

        visited = set()
        longest = 0

        for ch in s:
            if ch not in visited:
                visited.add(ch)
            
            else:
                visited.remove(ch)
                longest += 2
        
        if visited:
            longest += 1

        return longest

