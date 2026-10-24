# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 
            
            left = dfs(node.left)

            if node.val == subRoot.val:
                if isEqual(node, subRoot):
                    return True

            right = dfs(node.right)

            return left or right
        
        def isEqual(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1:
                return False
            
            if not root2:
                return False
            
            left = isEqual(root1.left, root2.left)
            right = isEqual(root1.right, root2.right)
                
            if root1.val == root2.val and left and right:
                return True
            
            return False

        if not dfs(root):
            return False
        else:
            return True

                