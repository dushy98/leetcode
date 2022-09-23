class Solution:
    def concatenatedBinary(self, n: int) -> int:
        M = 10 ** 9 + 7
        l, ans = 0, 0
        
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                l += 1
            ans = ((ans << l) | i) % M
        return ans
            
        