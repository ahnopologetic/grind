class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nn1 = set()
        nn2 = set()

        for n in nums1:
            if n not in nums2:
                nn1.add(n)
        
        for n in nums2:
            if n not in nums1:
                nn2.add(n)
        
        return [list(nn1), list(nn2)]
