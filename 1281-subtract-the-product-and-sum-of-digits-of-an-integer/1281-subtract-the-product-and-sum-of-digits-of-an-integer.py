class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        while n > 0:
            prod = prod * (n%10)
            sum = sum + (n%10)
            n = n // 10
            
        return prod - sum