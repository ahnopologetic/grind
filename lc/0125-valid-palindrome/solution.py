class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for i in s:
            if i.isalnum():
                word += i.lower()

        reverse = ''
        for i in range(len(word) - 1, -1, -1):
            reverse = reverse + word[i]

        return word == reverse
        
