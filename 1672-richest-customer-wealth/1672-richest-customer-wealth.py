class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for account in accounts:
            curr_cust_wealth = sum(account)
            max_wealth = max(max_wealth, curr_cust_wealth)
            
        return max_wealth