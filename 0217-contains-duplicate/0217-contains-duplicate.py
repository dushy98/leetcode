class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #comment to test autocommit
        return len(set(nums)) != len(nums)
        #return True if len(nums) != len(set(nums)) else False