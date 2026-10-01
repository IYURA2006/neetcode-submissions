# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2 4 6 8 10
        dummy = head
        # 2 4 6
        
        #find middle
        slow = head
        fast = head
        prev = None

        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = None
        else:
            return None

        #middle 
        #slow
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        node = ListNode()
        res = node
        while dummy:

            res.next = dummy
            dummy = dummy.next
            res = res.next

            res.next = prev
            prev = prev.next
            res = res.next

        if prev:
            res.next = prev
            prev = prev.next
            res = res.next
        
    
            