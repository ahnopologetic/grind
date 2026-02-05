class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # do as it is instructed.
        # use modulo
        res = []
        pos = {}
        n = len(nums)
        for i in range(n):
            val = nums[i]
            if val > 0:
                new_index = (i + val) % n
                # print(f"{new_index=} {nums[new_index]=}")
                pos[i] = nums[new_index]
            elif val < 0:
                new_index = (i - abs(val)) % n
                pos[i] = nums[new_index]
            else:
                pos[i] = val
        for j in range(len(nums)):
            res.append(pos[j])
        return res

