from collections import deque

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # [1, 0, 0] -> 10 0, 1 0 0, 100 -> not two bits
        # brute-force
        q = deque(bits)
        is_two_bit = True
        # moving from start, we have two choices
        # see it as one bit -> pop, set is_two_bit = False
        while q:
            first = q.popleft()
            if first == 0:
                is_two_bit = False
            else:
                q.popleft() # o(1)
                is_two_bit = True
        return not is_two_bit
        # see it as two bits -> pop
            # if bits[0] == 1: its two bits so we need the next bit. 
            # pop first two
            # set is_two_bit = True
        # after pop and if the bits array is empty, 
        # return is_two_bit

