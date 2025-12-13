class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # just take ith code, business line and isActive and validate
        # return them in sorted way
        res = [[], [], [], []]
        business_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        for i in range(len(code)):
            current_code = code[i]
            current_businessline = businessLine[i]
            current_isActive = isActive[i]

            conditions = (
                    current_code and (current_code.replace("_", "").isalnum() or current_code == "_")
                    and current_businessline in business_lines
                    and current_isActive is True
            )
                
            if conditions:
                idx = business_lines.index(current_businessline)
                res[idx].append(current_code) # lexicographically sort
                res[idx] = sorted(res[idx])
            

        return [item for sublist in res for item in sublist]


            

