class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # counter
        # if appeared, del
        # return that is count is 1

        c = Counter([i for i in range(1, len(nums) + 1)])
        for num in nums:
            c[num] -= 1
        
        return list([k for k, v in c.items() if v == 1])

