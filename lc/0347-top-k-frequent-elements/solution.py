class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use counter to count
        c = Counter()
        for num in nums:
            c[num] += 1
        # get k most common
        return [val for val, count in c.most_common(k)]
