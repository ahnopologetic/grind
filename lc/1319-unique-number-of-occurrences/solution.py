from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # when uniq occ, hash map
        data = defaultdict(int)
        for item in arr:
            data[item] += 1
        
        return len(data) == len(set(data.values()))

