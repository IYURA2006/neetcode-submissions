# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        def bfs (node):
            if not node:
                return []

            res = []
            queue = deque([root])


            while queue:
                
                level_len = len(queue)
                last_elem = queue[-1]
                res.append(last_elem.val)

                for i in range(level_len):
                    item = queue.popleft()

                    if item.left:
                        queue.append(item.left)

                    if item.right:
                        queue.append(item.right)
            return res
        return bfs(root)

