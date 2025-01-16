from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # now go for O(1) space. 
        result = majority = 0

        for num in nums:
            if not majority:
                result = num

            if num == result:
                majority += 1
            else: 
                majority -= 1
        
        
        return result
        
            
