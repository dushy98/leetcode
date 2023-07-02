class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #comment to test autocommit
        freq = Counter(nums)
        for num, freq in freq.items():
            if freq > 1:
                return True
        return False
        #return True if len(nums) != len(set(nums)) else False