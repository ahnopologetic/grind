class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # append common prefix when conditions are met
        res = ""
        shortest = min([len(s) for s in strs])
        for i in range(shortest):
            tokens = set()
            for s in strs:
                tokens.add(s[i])
            if len(tokens) > 1:
                break
            else:
                res += strs[0][i]
        
        return res


            
