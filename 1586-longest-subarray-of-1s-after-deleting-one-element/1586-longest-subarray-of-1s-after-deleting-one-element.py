class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)

        left = 0
        zeroes = 0
        ans = 0

        for right in range(length):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            ans = max(ans, right - left + 1 - zeroes)

        return ans - 1 if ans == length else ans 