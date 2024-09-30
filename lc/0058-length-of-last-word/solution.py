class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = [""]
        i = 0
        for idx, char in enumerate(s):
            if char != " ":
                words[i] += char

            else:
                if words[i]:
                    words.append("")
                    i += 1
        return len(words[-1])

