class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        dict = {}
        
        for i in range(len(s)):
            if s[i] in dict and start <= dict[s[i]]:
                start = dict[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            
            dict[s[i]] = i
        return max_len
        