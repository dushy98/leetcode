class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Bit Manipulation - approach 2
        ans = 0

        for i in range(32):
            bit_sum = 0
            for num in nums:
                # Convert the number to 2's complement for large test cases
                if num < 0:
                    num = num&(2**32-1)
                bit_sum += (num >> i) & 1
            bit_sum %= 3 
            ans |= bit_sum << i

        if ans >= 2**31:
            ans -= 2**32
            
        return ans
