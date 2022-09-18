class Solution:
    def trap(self, height: List[int]) -> int:
        h_len = len(height)
        biggest_left: list[int] = [height[0]] * h_len
        biggest_right: list[int] = [height[-1]] * h_len

        for i in range(1, h_len):
            biggest_left[i] = max(biggest_left[i-1], height[i])
            biggest_right[-i-1] = max(biggest_right[-i], height[-i-1])
        
        return sum(min(biggest_left[i], biggest_right[i]) - height[i] for i in range(h_len))