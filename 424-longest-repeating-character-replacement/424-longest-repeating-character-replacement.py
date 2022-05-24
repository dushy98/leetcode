class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = i = 0
        count = collections.Counter()
        
        for j in range(len(s)):
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])
            if j - i + 1 > maxf + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i
        