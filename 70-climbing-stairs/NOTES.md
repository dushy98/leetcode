```
class Solution:
def climbStairs(self, n: int) -> int:
# using top-down memoization
memo = {}
memo[1] = 1
memo[2] = 2
def climb(n):
if n in memo:           # check if recusion done before in look-up table
return memo[n]
else:                   # store the recusrssion function in look-up table and return
memo[n] = climb(n-1) + climb(n-2)
return memo[n]
return climb(n)
​
```