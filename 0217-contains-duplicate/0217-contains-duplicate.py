class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #comment to test autocommit
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        #return True if len(nums) != len(set(nums)) else False