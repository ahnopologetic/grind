class Solution:
    def reverseWords(self, s: str) -> str:
        # two pointer...
        words = s.strip().split()
        result = []

        for i in range(len(words) - 1, -1, -1):
            result.append(words[i])
        
        return " ".join(result)


