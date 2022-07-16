class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for a in encoded:
            res.append(res[-1] ^ a)
        
        return res