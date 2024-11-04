class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        buffer = defaultdict(int)

        for char in s:
            buffer[char] += 1
        
        for char in t:
            if buffer[char] == 1:
                del buffer[char]
            
            else:
                buffer[char] -= 1
            
        
        print(buffer)
        return not buffer
