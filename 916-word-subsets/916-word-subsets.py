class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        c_b = reduce(operator.or_, (Counter(w) for w in words2))
        return [a for a in words1 if c_b & Counter(a) == c_b]