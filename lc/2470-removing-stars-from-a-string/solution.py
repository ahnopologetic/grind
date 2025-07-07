class Solution:
    def removeStars(self, s: str) -> str:
        # use stack
        # if we meet star, pop the top
        # else: add to the stack
        
        stack = []
        result = ""

        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                stack.pop(-1)

        return "".join(stack)
