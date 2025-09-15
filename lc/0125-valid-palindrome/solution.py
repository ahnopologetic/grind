class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        new_s = ""
        for ch in s:
            if ch.isalnum():
                new_s += ch
        
        left, right = 0, len(new_s) - 1
        ans = True
        while left < right:
            if new_s[left] != new_s[right]:
                ans = False
                break
            else:
                left += 1
                right -= 1

        return ans
