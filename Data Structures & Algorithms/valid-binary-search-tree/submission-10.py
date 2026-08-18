# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, left_boundary, right_boundary):
            if not node:
                return True

            if not (left_boundary < node.val < right_boundary):
                return False
            
            return isValid(node.left, left_boundary , node.val) and isValid(node.right, node.val, right_boundary)

        return isValid(root, float("-inf"), float("inf"))        




        
        
        
        
        
        
        #prev = None
        # def dfs(node):
        #     if not node:
        #         return True
            
        #     res1 = dfs(node.left)
        #     nonlocal prev
        #     if prev is not None and prev >= node.val:
        #         return False
        #     else:
        #         prev = node.val

        #     if not res1:
        #         return False 

        #     res2 = dfs(node.right)

        #     return res1 and res2


        # res = dfs(root)
        # return res


     #   5
  #  1       4
      #    3   6