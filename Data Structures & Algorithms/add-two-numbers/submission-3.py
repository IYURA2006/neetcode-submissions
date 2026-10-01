# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        
        dummy = res
        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            total = val1 + val2 + carry
            carry = 0

            if total > 9:
                total = total % 10
                carry += 1

            dummy.next = ListNode(total)
            dummy = dummy.next

            if l1:
                l1 = l1.next
            if l2:

                l2 = l2.next
    
        return res.next

        # 3 2 1.  
        # 6 5 4
        # 