class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # [1, 10, 100, 9] => 9100101, 
        # sort by string higher value, and append
        sn = sorted([str(num) for num in nums], key=lambda x: x*10, reverse=True)
        if sn[0] == "0":
            return "0"
        return "".join(sn)
