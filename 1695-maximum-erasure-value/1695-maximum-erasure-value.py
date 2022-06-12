class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        begin, end, Set, summ = 0, 0, set(), 0
        ans = 0
        
        # 2-pointer or sliding window approach 
        while end < len(nums):
            if nums[end] not in Set:
                summ += nums[end]
                Set.add(nums[end])
                end += 1
                ans = max(ans, summ)
            else:
                summ -= nums[begin]
                Set.remove(nums[begin])
                begin += 1
            
        return ans
        