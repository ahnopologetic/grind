class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # basic stack
        # when it bumps into operator, pop 2 (a, b) -> a (operator) b = c -> c goes back to stack
        # repeat until the stack is empty
        stack = []
        operators = "+*/-"
        for token in tokens:
            if token in operators:
                b = int(stack.pop())
                a = int(stack.pop())

                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "*":
                    res = a * b
                elif token == "/":
                    res = int(a / b)
                else:
                    raise ValueError("nope")
                stack.append(res)
                continue
            stack.append(token)
            
            
        
        return int(stack[-1])

            

            

