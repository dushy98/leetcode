class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        num = 0
        
        for v in nums:
            if v in repeat:
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]
                
                repeat[v] += 1
                
            else:
                repeat[v] = 1
        return num
        