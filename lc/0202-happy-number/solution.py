class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            result = 0
            while n > 0:
                last = n % 10
                result += last * last
                n = n//10
            return result

        slow = square(n)
        fast = square(square(n))

        while fast != 1 and slow != fast:
            slow = square(slow)
            fast = square(square(fast))
        
        return fast == 1
