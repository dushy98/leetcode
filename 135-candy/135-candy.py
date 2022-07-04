class Solution:
    def candy(self, ratings: List[int]) -> int:
        n, res = len(ratings), [1]*len(ratings)
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                res[i+1] = max(1 + res[i], res[i+1])
                
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                res[i] = max(1 + res[i+1], res[i])
                
        return sum(res)
        