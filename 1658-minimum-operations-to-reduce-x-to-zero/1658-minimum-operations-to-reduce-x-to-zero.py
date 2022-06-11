class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        cumSum = [0] + list(accumulate(nums))
        dict_ = {c:i for i,c in enumerate(cumSum)}
        
        goal = cumSum[-1] -x
        ans = -float("inf")
        
        if goal < 0: return -1
        
        for num in dict_:
            if num + goal in dict_:
                ans = max(ans, dict_[num + goal] - dict_[num])
                
        return len(nums) - ans if ans != -float("inf") else -1
        