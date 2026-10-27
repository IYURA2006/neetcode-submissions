"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        nodes = {}
        start_pointer = Node(0)
        traversal_pointer = start_pointer

        dummy = head

        while dummy:
            newNode = Node(dummy.val)
            traversal_pointer.next = newNode

            traversal_pointer = traversal_pointer.next
            nodes[dummy] = (newNode)
        
            dummy = dummy.next


        traversal_pointer = start_pointer.next
        
        while head:
            pos = head.random
         
            if pos:
                traversal_pointer.random = nodes[pos]
            else:
                traversal_pointer.random = None
            
            traversal_pointer = traversal_pointer.next
            head = head.next

        return start_pointer.next

