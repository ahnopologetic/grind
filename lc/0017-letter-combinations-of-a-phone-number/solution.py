class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking 
        # map 
        # when we visited all possible letters of the last digit, backtrack
        if not digits:
            return []


        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        n = len(digits)
        result = []

        def explore(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            
            else:
                for letter in letters[next_digits[0]]:
                    explore(combination + letter, next_digits[1:])
        

        explore("", digits)
        return result



