class Solution:
    def countBits(self, num: int) -> List[int]:
        return list(map(lambda x: bin(x).count("1"), list(map(lambda x: x, range(num+1)))))
