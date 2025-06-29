class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: str, b: str):
            while b:
                if a[:len(b)] != b and b[:len(a)] != a:
                    a = ""
                    break
                a, b = b, a.replace(b, "", 1)
            
            return a
        
        return gcd(str1, str2)
