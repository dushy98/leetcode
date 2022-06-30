class Solution:
    def countBits(self, n: int) -> List[int]:
        nextOrder = 2
        tracker = 0
        counter = [0]*(n + 1)
        
        for i in range(1, n+1):
            if i == nextOrder:
                nextOrder *= 2
                tracker = 0
            counter[i] = counter[tracker] + 1
            tracker += 1
        return counter

        