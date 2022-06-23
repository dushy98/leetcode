class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # using greedy approach
        heap, total = [], 0
        for dur, end in sorted(courses, key=lambda el: el[1]):
            if dur + total <= end:
                total += dur
                heappush(heap, -dur)
            elif heap and -heap[0] > dur:
                total += dur + heappop(heap)
                heappush(heap, -dur)
        return len(heap)        

        