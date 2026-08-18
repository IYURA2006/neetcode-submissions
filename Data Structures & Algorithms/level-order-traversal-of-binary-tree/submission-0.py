# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        



        def bfs (node):
            if not node:
                return []

            queue = deque([node])
            res = []
            while queue:
                
                level_elems = len(queue)
                cur_level = []
                for i in range(level_elems):
                    
                    item = queue.popleft()

                    cur_level.append(item.val)

                    if item.left:
                        queue.append(item.left)
                    
                    if item.right:
                        queue.append(item.right)
                    
                res.append(cur_level)
            return res
        res = bfs(root)

        return res