class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False for _ in range(len(candies))]
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max(candies):
                res[i] = True
        
        return res
        