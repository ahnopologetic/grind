class Solution:
    def isValid(self, s: str) -> bool:
        hm = dict(("()", "{}", "[]"))
        stack = []

        for char in s:
            if char in hm.keys():
                stack.append(char)
            elif len(stack) == 0 or char != hm[stack.pop()]:
                return False
        
        return len(stack) == 0
