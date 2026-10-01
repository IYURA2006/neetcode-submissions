# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        prev = None

        while cur != None:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp
        # 0 -> 1 -> 2 -> 3
        # cur -> 2
        # prev -> 1
        return prev