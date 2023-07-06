class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0

        sum=0
        res=float('inf')

        for r in range(0, len(nums)):
            sum+=nums[r]

            while sum >= target:
                res = min(res,r-l+1)
                sum-=nums[l]
                l+=1
        
        return res if res != float('inf') else 0