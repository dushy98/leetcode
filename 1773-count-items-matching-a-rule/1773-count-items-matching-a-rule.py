class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        for item in items:
            if item[d[ruleKey]] == ruleValue:
                count += 1
        return count
        
        #return sum(1 for item in items if item[d[ruleKey]] == ruleValue)
        