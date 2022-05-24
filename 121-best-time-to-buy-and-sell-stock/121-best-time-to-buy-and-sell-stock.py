class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # buy
        right = 1 #sell
        max_profit = 0
        
        while right < len(prices):
            cur_profit = prices[right] - prices[left] # current profit
            if prices[left] < prices[right]:
                max_profit = max(cur_profit,max_profit)
            else:
                left = right
            right = right + 1
        return max_profit
                
        
        
"""
  prices  7  1  6  4  3  1
          0  1
          
      left   right
  
 
"""
        