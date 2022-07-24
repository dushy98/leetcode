class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        num = n
        while num > 0:
            prod = prod * (num%10)
            sum = sum + (num%10)
            num = num // 10
            
        return prod - sum