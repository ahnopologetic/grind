class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # simple math
        # have a res as a total, think income as a budget, for each bracket decrement from income and repeat it until it becomes less than 0

        res = 0
        i = 0
        while income > 0:
            if i == 0:
                amount = min(income, brackets[i][0])
                res += amount * (brackets[i][1] / 100)
                income -= amount
            else:
                tax_diff = brackets[i][0] - brackets[i-1][0]
                amount = min(income, tax_diff)
                res += amount * (brackets[i][1] / 100)
                income -= amount
            i += 1
        return res


        return res
