# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, target1, target2):
            if not node:
                return False

            if node.val == target1.val or node.val == target2.val:
                return node

            left = dfs(node.left, target1, target2)
            right = dfs(node.right, target1, target2)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
         
            return 


        return dfs(root,p, q)