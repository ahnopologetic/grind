from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {("t", "e", "a"), }
        result = defaultdict(list)
        for string in strs:
            token = tuple(sorted([c for c in string]))
            result[token] += [string]
        
        return list(result.values())

        
