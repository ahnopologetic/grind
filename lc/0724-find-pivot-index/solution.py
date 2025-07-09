class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls, rs = 0, sum(nums)

        for i, elem in enumerate(nums):
            rs -= elem
            if ls == rs:
                return i
            ls += elem
        
        return -1

