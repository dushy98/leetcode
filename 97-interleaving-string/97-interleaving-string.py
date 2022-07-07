class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): 
            return False
        
        m, n = len(s1), len(s2)
        dp, dpPrev = [False] * (n+1), [False] * (n + 1)
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                dp[j] = False
                if i == m and j == n:
                    dp[n] = True
                if i < m and s1[i] == s3[i+j]:
                    dp[j] |= dpPrev[j]
                if j < n and s2[j] == s3[i+j]:
                    dp[j] |= dp[j + 1]
            dp, dpPrev = dpPrev, dp
        return dpPrev[0]
        