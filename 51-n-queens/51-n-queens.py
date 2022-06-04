class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):       # Backtracking
        if index == len(nums):             
            res.append(path)
            return                          
        
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path + [tmp[:i] + "Q" + tmp[i+1:]], res)
                
    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n-i or nums[i] == nums[n]:
                return False
        return True
                
                
        
        