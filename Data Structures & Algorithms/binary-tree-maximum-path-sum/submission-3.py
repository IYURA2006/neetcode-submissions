# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maximumSum = float("-inf")
        def dfs(node):
            nonlocal maximumSum
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            straight_line = node.val + max(left, right)

            arch = left + right + node.val

            maximumSum = max(arch, maximumSum)
            return straight_line
        dfs(root)
        return maximumSum
        
