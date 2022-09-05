"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None: 
            return []
        
        dq = deque([root])
        ans = []
        while dq:
            level = []
            for _ in range(len(dq)):
                curr = dq.popleft()
                level.append(curr.val)
                for child in curr.children:
                    dq.append(child)
            ans.append(level)
        return ans