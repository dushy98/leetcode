# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def preorder(node, path):
            nonlocal count
            if node:
                path = path ^ (1 << node.val)
                
                if node.left is None and node.right is None:
                    if path & (path - 1) == 0:
                        count += 1
                        
                else: 
                    preorder(node.left, path)
                    preorder(node.right, path)
        count = 0
        preorder(root, 0)
        return count