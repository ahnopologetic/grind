class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = "".join([ch for ch in list(s.lower().replace(" ", "")) if ch.isalnum()])
        
        start, end = 0, len(sanitized) - 1
        while start < end:
            if sanitized[start] != sanitized[end]:
                return False

            start += 1
            end -= 1
        return True
