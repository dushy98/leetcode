class Solution:
    def hammingWeight(self, n: int) -> int:
        # using bit manupilation
        count = 0
        while n:
            n = n & (n-1)
            count = count + 1
        return count
        
        