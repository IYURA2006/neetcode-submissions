# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        minimum_difference = float('inf')
        previousNode = None
        def dfs(node):
            nonlocal minimum_difference
            nonlocal previousNode
            if not node:
                return 
            
            left = dfs(node.left)
            if previousNode is not None:
                minimum_difference = min(node.val - previousNode, minimum_difference)
            previousNode = node.val

            right = dfs(node.right)
        dfs(root)
        return minimum_difference
            