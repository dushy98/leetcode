class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # check input
        if not cost:
            return 0
        
        # memo to store results for each index
        dp = [0] * len(cost)
        
        dp [0] = cost[0]
        
        # dp 1 will be 1
        if len(cost) >= 2:
            dp[1] = cost[1]
        
        # since we can come only from the previous 2 stairs to this stair 
        # we add the minimum of these 2 to the cost 
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        #similarly the last step can be stepped on from previous 2 steps only
        # hence we return minimum of them
        return min(dp[-1], dp[-2])
        