class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        Mod = 10**9 + 7
        dp = [0] + [1] * (k + 1)
        for N in range(2, n + 1):
            new = [0]
            for K in range(k + 1):
                v = dp[K + 1]
                v -= dp[K - N +1] if K >= N else 0
                new.append((new[-1] + v) % Mod)
            dp = new
        return (dp[k + 1] - dp[k]) % Mod
        