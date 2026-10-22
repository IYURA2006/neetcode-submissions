# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        numberGoodNodes = 0

        def dfs (node, cur_max):
            nonlocal numberGoodNodes
            if not node:
                return 

          

            if cur_max <= node.val:
                numberGoodNodes += 1
                print(node.val)
                cur_max = node.val


            dfs(node.left, cur_max)
            
            dfs(node.right, cur_max)

        dfs(root, -float('inf'))
        
        return numberGoodNodes