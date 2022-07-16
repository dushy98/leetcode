class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join([s[i] for i in sorted(list(range(len(s))), key = lambda x:indices[x])])