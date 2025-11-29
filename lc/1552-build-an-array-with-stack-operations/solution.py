class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # [1, 2, 5], 5
        # push, push, push, pop, push, pop, push
        # push, push, push, push, pop, pop, push

        res = []
        max_target = max(target)

        for i in range(1, n+1):
            if i not in target: res += ["Push", "Pop"]
            else: res += ["Push"]

            if i == max_target:
                break
        return res
