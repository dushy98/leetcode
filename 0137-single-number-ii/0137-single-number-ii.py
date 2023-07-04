class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #brute force - approach 1
        count = defaultdict(int)

        for i in nums:
            count[i] += 1
        
        for i, freq in count.items():
            if freq == 1:
                return i
        
        return -1
