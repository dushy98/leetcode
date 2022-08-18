class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0
        
        for i, count in enumerate(sorted(collections.Counter(arr).values(), reverse = True)):
            total_count += count
            if total_count >= len(arr) // 2:
                return i + 1 
        
        
        return 0