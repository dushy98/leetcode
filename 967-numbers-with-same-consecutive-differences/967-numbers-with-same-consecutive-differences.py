class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        cur = range(1, 10)
        for i in range(N-1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + K, x % 10 - K] if 0 <= y <= 9}
        return list(cur)