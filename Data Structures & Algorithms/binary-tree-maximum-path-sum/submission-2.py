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
            
            left = dfs(node.left)
            right = dfs(node.right)

            straight_line = 0
            arch = 0

            #case 1 all

            if left > 0 and right > 0:
                arch += left + right + node.val

            #case just node + left

            elif left > 0:

                arch += left + node.val
            #case just node + right

            elif right > 0:

                arch += right + node.val
            #case just node

            else:

                arch += node.val

            score = max(left, right)
            if score > 0:
                straight_line = score + node.val
            else:
                straight_line = node.val

            maximumSum = max(arch, maximumSum)
            return straight_line
        dfs(root)
        return maximumSum
        
