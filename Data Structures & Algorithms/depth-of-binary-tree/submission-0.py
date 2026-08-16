# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def bfs(node):
            queue = deque([root])
            if not root:
                return 0
            levels = 0
            while len(queue) > 0:
                
                cur_length = len(queue)
                #need to process the whole level 
                for item in range(cur_length):
                    node = queue.popleft()
                    print(node.val)
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                levels +=1

            return levels

        res = bfs(root)
        return res