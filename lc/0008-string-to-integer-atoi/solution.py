class Solution:
    def myAtoi(self, s: str) -> int:
        # verbatim
        s = s.strip()
        if not s:
            return 0

        sign, i, result = 1, 0, 0

        if s[0] and s[0] in ("-", "+"):
            sign = sign * -1 if s[0] == "-" else sign
            if sign < 0:
                s = s.replace("-", "", 1)
            else:
                s=s.replace("+", "", 1)
        
        for ch in s:
            if ch == "0" and not result:
                continue
            if not ch.isdigit():
                break
            result = result * 10 + int(ch)

            if result * sign > 2**31 -1:
                return 2**31 -1
            if result * sign < -2**31:
                return -2**31
        if not result:
            return 0
        return result * sign
        

