class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # difference between substring and subsequence
        return 2 - (s == s[::-1]) - (s == "")
        