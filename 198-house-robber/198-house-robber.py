class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2. constant space using 2 variables
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(num + prev, curr)
        return curr
