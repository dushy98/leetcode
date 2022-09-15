class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt, ans = Counter(changed), []
        if len(changed) % 2:
            return []
        
        for x in sorted(cnt.keys()):
            if cnt[x] > cnt[x * 2]:
                return []
            if x == 0:
                if cnt[x] % 2:
                    return []
                else:
                    ans += [0] * (cnt[x] // 2 )
            else:
                ans += [x] * cnt[x]
            cnt[2 * x] -= cnt[x]
        return ans