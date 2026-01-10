class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # list of combination
        # n = 4
        # maxdep = 4, maxdep = 3, maxdep = 2, maxdep = 1
        # backtracking

        # open, closed
        # always closed < open: 
        # 
        stack = []
        res = []

        def backtrack(op, cl):
            if n == op == cl:
                res.append("".join(stack))
                return
            if op < n:
                stack.append("(")
                backtrack(op + 1 , cl)
                stack.pop()
            
            if cl < op:
                stack.append(")")
                backtrack(op, cl + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
