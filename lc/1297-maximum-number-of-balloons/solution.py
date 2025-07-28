class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # # dictionary of counter popping when char encountered
        # # when it is emptied, fill up again and count up
        # target = "balloon"
        # tokens = {}
        # result = 0

        # def fillup(d: dict):
        #     for ch in target:
        #         if ch in tokens:
        #             d[ch] += 1
        #         else:
        #             d[ch] = 1
            
        #     return d
        

        # fillup(tokens)

        # for ch in text:
        #     if ch in tokens:
        #         if tokens[ch] == 1:
        #             del tokens[ch]
        #         else:
        #             tokens[ch] -= 1
        #     if not tokens:
        #         result += 1
        #         fillup(tokens)
            
        
        # return result

        return min(
            text.count('b'), 
            text.count('a'), 
            text.count('l') // 2, 
            text.count('o') // 2, 
            text.count('n'), 
            )
            
        
        
        


