class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        start, end = 0, len(num) - 1
        while (start < end):
            if num[start] != num[end]:
                return False
            start += 1
            end -= 1
        return True
