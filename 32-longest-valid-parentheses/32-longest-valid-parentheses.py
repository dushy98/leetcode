class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # check base case
        if not s:
            return 0
        stack = [-1]
        max_len = 0 
        
        for i,ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    curr_len = i - stack[len(stack) - 1]
                    max_len  = max(curr_len, max_len)
        return max_len
        
        
        
        