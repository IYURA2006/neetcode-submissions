# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        traversal = head
        while traversal:
            traversal = traversal.next
            length += 1

        counter = length - n
        i = 0

        node = ListNode()
        node.next = head

        dummy = node

        while dummy:
            print(dummy.val)
            if i == counter:
                break
            dummy = dummy.next
            i += 1
        
        if n <= 1:
            dummy.next = None
        else:
            dummy.next = dummy.next.next

        return node.next