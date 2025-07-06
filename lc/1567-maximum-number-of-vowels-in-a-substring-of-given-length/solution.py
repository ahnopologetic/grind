class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeoui')
        max_vowel = 0
        count = 0

        for i in range(len(s)):
            if s[i] in vowel:
                count += 1
            
            if i >= k:
                if s[i - k] in vowel:
                    count -= 1
            max_vowel = max(max_vowel, count)
        
        return max_vowel
