class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # op = []
        n = []
        operators = list("+-*/")

        for token in tokens:
            if token in operators:
                b = int(n.pop())
                a = int(n.pop())
                
                new_token = None
                if token == "+":
                    new_token = a + b
                elif token == "-":
                    new_token = a - b
                elif token == "*":
                    new_token = a * b
                else:
                    new_token = a / b    
                
                n.append(new_token)
            else:
                n.append(token)
        return int(n[-1])
