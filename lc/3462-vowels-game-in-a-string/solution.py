class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # count all vowels
        # greedy approach as many as possible
        # 7 -> 3 -> 2 -> 1
        return any([ch in 'aeiou' for ch in s])

