class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 or n == 0
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1

        for i in range(1, len(flowerbed) - 1):
            if n == 0:
                break
            if not flowerbed[i-1] and not flowerbed[i+1] and flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n -= 1
        
        return n <= 0

