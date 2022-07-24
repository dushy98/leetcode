class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        num = n
        for i in range(len(str(n))):
            prod = prod * (num%10)
            sum = sum + (num%10)
            num = num // 10
            
        return prod - sum