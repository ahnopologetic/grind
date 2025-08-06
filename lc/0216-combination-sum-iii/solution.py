class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # backtracking
        # base case: sum of first n digits < k, then return []
        # explore(comb: [], digits: [])
        # if len(comb) == k, push to result
        # else
        # for i, digit in enumerate(digits):
        #   explore(comb + [digit], digits[i:])
        # # how to backtrack?

        nums = [i for i in range(1, 10)]
        if sum(nums[:k]) > n:
            return []
        result = []

        def backtrack(comb: list[int], digits: list[int]):
            if len(comb) == k:
                if sum(comb) == n:
                    result.append(comb)
                return
            else:
                for i, digit in enumerate(digits):
                    
                    if digit <= n - sum(comb):
                        backtrack(comb + [digit], digits[i+1:])
                    else:
                        return
        
        backtrack([], nums)
        return result
        
