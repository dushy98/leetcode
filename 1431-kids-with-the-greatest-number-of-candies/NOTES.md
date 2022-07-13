```
res = [False for _ in range(len(candies))]
for i in range(len(candies)):
if (candies[i] + extraCandies) >= max(candies):
res[i] = True
return res
```