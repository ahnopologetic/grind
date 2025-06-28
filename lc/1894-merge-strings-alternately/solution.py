class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        m, n = len(word1), len(word2)

        for i in range(max(m, n)):
            if i < m:
                result += word1[i]
                
            if i < n:
                result += word2[i]
        
        return result
