# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return 
        res = []

        def BSTsearch (node, num1, num2):
            res.append(node.val)
            if node.val > num1.val and node.val > num2.val:
                return BSTsearch(node.left, num1, num2)
            
            if node.val < num1.val and node.val <num2.val:
                return BSTsearch(node.right, num1, num2)

            else:
                return node
            
            

        res = BSTsearch(root, p, q)
        return res
        