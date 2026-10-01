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
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            
            total = val1 + val2 + carry
            print(total)
            print(carry)
            carry = 0

            if total > 9:
                total = total % 10
                carry += 1

            dummy.next = ListNode(total)
            dummy = dummy.next

            l1 = l1.next
            l2 = l2.next
    

        if carry == 1:
            if l1:
                    while l1 and carry == 1:
                        total = l1.val + carry
                        carry = 0

                        if total > 9:
                            carry += 1
                            total = total % 10

                        l1.val = total
                        
                        dummy.next = l1
                        dummy = dummy.next
                        l1 = l1.next
                        
            elif l2:
                    while l2 and carry == 1:
                        total = l2.val + carry
                        carry = 0

                        if total > 9:
                            carry += 1
                            total = total % 10

                        l2.val = total

                        dummy.next = l2
                        dummy = dummy.next
                        l2 = l2.next
                    

        if carry == 1:
            dummy.next = ListNode(1)
        
        if carry == 0:
            dummy.next = l1 or l2

        return res.next


        # 3 2 1.  
        # 6 5 4
        # 