from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # o1: all characters are present for both
        # o2: freq of characters is the same

        # o1 = all([True if ch in word2 else False for ch in word1])
        # counter1 = {}
        # for ch in word1:
        #     if ch in counter1:
        #         counter1[ch] += 1
        #     else:
        #         counter1[ch] = 1
        # counter2 = {}
        # for ch in word2:
        #     if ch in counter2:
        #         counter2[ch] += 1
        #     else:
        #         counter2[ch] = 1
        # o2 = set(counter1.values()) == set(counter2.values())
        # return o1 and o2

        m1 = Counter(word1)
        s1 = list()
        m2 = Counter(word2)

        for i in m1:
            if i not in m2:
                return False
            s1.append(m1[i])
        
        for i in m2:
            if m2[i] not in s1:
                return False
            
            else:
                s1.remove(m2[i])
        
        return True
