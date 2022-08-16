class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        cnt = collections.Counter(s)
        
        # single enumerate loop of python
        for i, char in enumerate(s):
            if cnt[char] == 1:
                return i
        return -1