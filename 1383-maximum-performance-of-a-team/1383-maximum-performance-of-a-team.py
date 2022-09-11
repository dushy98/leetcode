class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        curr_sum, h = 0, []
        ans = -float('inf')
        
        for i,j in sorted(zip(efficiency, speed), reverse = True):
            while len(h) > k-1:
                curr_sum -= heappop(h)
            heappush(h, j)
            curr_sum += j
            ans = max(ans, curr_sum * i)
        
        return ans % (10**9+7)