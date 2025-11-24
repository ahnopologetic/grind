class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for ch in s:
            if stack and ch in pairs:
                token = stack.pop()
                if pairs[ch] != token:
                    return False

            else:
                stack.append(ch)
        
        return not stack


