class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        ans = [[0] * (N-2) for i in range(N-2) ]
        
        for i in range(N-2):
            for j in range(N-2):
                maxV =  max(grid[i][j],
                            grid[i][j+1],
                            grid[i+1][j+1],
                            grid[i+1][j+2],
                            grid[i+1][j],
                            grid[i+2][j+2],
                            grid[i][j+2],
                            grid[i+2][j+1],
                            grid[i+2][j])
                
                ans[i][j] = maxV
                
        return ans