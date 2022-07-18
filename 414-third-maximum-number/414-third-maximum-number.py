class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) > 2:
            return sorted(nums)[-3]
        else:
            return max(nums)