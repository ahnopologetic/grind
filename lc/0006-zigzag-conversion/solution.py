class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        curr = 0 # current rows
        go_down = False

        for ch in s:
            rows[curr] += ch
            if curr == 0 or curr == numRows - 1:
                go_down = not go_down
        
            curr += 1 if go_down else -1 
        
        return "".join(rows)
