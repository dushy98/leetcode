class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = []
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            runSum.append(total)
        return runSum
