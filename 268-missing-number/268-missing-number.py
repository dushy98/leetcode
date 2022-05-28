class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0 
        for i in range(len(nums)):
            sum += nums[i]
            
        return int(len(nums) * (len(nums) + 1) / 2 - sum)
        

            