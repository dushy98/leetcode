class Solution:
    def minDeletions(self, s: str) -> int:
        count, res, set_ = collections.Counter(s), 0, set()
        for char, freq in count.items():
            while freq > 0 and freq in set_:
                freq -= 1
                res += 1
            set_.add(freq)
        return res
        