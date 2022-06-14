class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[0]* (n+1) for _ in range(m+1) ]
        for i,a in enumerate(word1,1):
            for j,b in enumerate(word2,1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+(a==b))
            
        return m + n - 2 * dp[-1][-1]

        