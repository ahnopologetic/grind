class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        src_temp = ""
        dest_temp = ""
        src = 0
        dest = len(s) - 1
        mid = (src + dest) // 2

        while src <= mid:
            src_temp = s[src]
            dest_temp = s[dest]

            s[src] = dest_temp
            s[dest] = src_temp

            src += 1
            dest -= 1
        
        return s

            

        
