class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result = []

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in d:
                d[sorted_str] = [str]
            else:
                d[sorted_str] += [str]
        
        return [anagram for anagram in d.values()]

