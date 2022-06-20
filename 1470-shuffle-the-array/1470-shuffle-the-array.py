class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        idx = lambda i: i*2 if i<n else (i-n)*2+1
        for i in range(2*n):
            j = i
            while nums[i] >= 0:
                j=idx(j)
                nums[i], nums[j] = nums[j], -nums[i]
        
        for i in range(2*n):
            nums[i]=-nums[i]
        return nums
        
        
            
        