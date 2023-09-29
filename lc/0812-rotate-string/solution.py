class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True

        rotated = s[1:] + s[0]
        while (rotated != s):
            if rotated == goal:
                return True
            rotated = rotated[1:] + rotated[0]
        return False
