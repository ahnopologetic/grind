class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            # it is over 10, continue
            if digits[i] + 1 > 9:
                digits[i] = 0
            # else, break
            else:
                digits[i] = digits[i] + 1
                return digits

            # if i = 0, return [1] + digits
            if i == 0:
                return [1] + digits
