class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # count -> gcd
        c = Counter()
        for elem in deck:
            c[elem] += 1
        
        vals = list(c.values())
        curr_gcd = float('-inf')
        
        for val in vals:
            if curr_gcd == float('-inf'):
                curr_gcd = val
                continue
            
            if val != curr_gcd:
                curr_gcd = math.gcd(val, curr_gcd)
            
        return curr_gcd != 1
        
        
