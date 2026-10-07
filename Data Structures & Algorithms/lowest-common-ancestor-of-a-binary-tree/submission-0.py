# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []
        def dfs(node, target):
            if not node:
                return False
            
            res.append(node)

            if node.val == target.val:
                return True

            if dfs(node.left, target) or dfs(node.right, target):
                return True
            
            #if we reach here backtrack
            res.pop()
            return False


        dfs(root, p)
        res1 = res.copy()
        res = []
        dfs(root,q)
        res2 = res.copy()
        for i in range(min(len(res1), len(res2))):
            if res1[i].val != res2[i].val:
                return res1[i-1]


        index = min(len(res1), len(res2))
        return res1[index - 1]
        