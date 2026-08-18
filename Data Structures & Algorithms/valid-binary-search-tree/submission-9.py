# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def dfs(node):
            if not node:
                return True
            
            res1 = dfs(node.left)
            nonlocal prev
            if prev is not None and prev >= node.val:
                return False
            else:
                prev = node.val

            if not res1:
                return False 
            res2 = dfs(node.right)

            return res1 and res2


        res = dfs(root)
        return res


     #   5
  #  1       4
      #    3   6