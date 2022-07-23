class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr, ans = sorted(nums), []
        
        for num in nums:
            i = bisect_left(arr,num)
            ans.append(i)
            del arr[i]
            
        return ans