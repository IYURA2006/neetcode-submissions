# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import string

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        lowercase = string.ascii_lowercase
        if not root:
            return ""
        res = []
        def dfs (node, cur_str):

            stack = []
            visited = set()
            stack.append((node, cur_str))

            while stack:
                item, str1 = stack.pop()

                cur_str = lowercase[item.val] + str1
    
                if not item.left and not item.right:
                    res.append(cur_str)
                    pass
                
                if item.left:
                    stack.append((item.left, cur_str))
                
                if item.right:
                    stack.append((item.right, cur_str))
        
        dfs(root, '')

        res.sort()
        return res[0]
