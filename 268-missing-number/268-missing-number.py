class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # one line O(1) solution using maths
        return int(len(nums) * (len(nums) + 1) / 2 - sum(nums))
        

            