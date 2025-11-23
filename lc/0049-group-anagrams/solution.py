class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            chars = [""] * 26
            for ch in s:
                chars[ord(ch) - ord('a')] += ch
            anagram = "".join(chars)
            if anagram in res:
                res[anagram].append(s)
            else:
                res[anagram] = [s]
        return list(res.values())



