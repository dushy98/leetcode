```
class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
dictionary = {}
for i in range(len(nums)):
if nums[i] in dictionary:
return [dictionary[nums[i]], i]
else:
dictionary[target - nums[i]] = i
```
​