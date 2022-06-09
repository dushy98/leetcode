class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2-pointer approach, because array is sorted
        left, right = 0, len(numbers) - 1
        
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left+1, right+1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1
        