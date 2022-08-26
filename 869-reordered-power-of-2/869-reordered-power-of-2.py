class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = collections.Counter(str(n))
        return any(count == collections.Counter(str(1 << b)) for b in range(31) )
        