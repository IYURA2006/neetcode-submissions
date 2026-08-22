# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #we need to find longest max(left + longest right + 1)
        self.longestWay = 0

        def longestSubTree (root):
            if not root:
                return 0

            leftChildren = longestSubTree(root.left) 
            rightChildren = longestSubTree(root.right)

            self.longestWay = max(leftChildren + rightChildren, self.longestWay)
            return 1 + max(leftChildren, rightChildren)
        longestSubTree(root)
        return self.longestWay
