class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        index = -1
        count = 0
        
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i+1]:
                index = i
                count += 1
                
        if count == 0:
            return True
        
        elif count == 1:
            if index == 0 or index == len(nums)-2:
                return True
            elif nums[index-1] < nums[index+1] or (index+2 < len(nums) and nums[index] < nums[index+2]):
                return True
        
        return False