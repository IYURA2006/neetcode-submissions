# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def get_reversed(list_linked : ListNode) -> ListNode:
            pointer = list_linked
            prev = None
            while pointer:
                next_node = pointer.next
                pointer.next = prev

                prev = pointer
                pointer = next_node

            return prev
    
        item1 = get_reversed(l1)
        pointer = item1

        item2 = get_reversed(l2)

        carry = 0
        prev = None
        while item1 or item2 or carry:
            total = 0
            if item1:
                total += item1.val
                prev = item1
            else:
                prev.next = ListNode(0)
                prev = prev.next
                item1 = prev

            if item2: 
                total += item2.val

            total += carry
            
            carry = total // 10
            total = total % 10

            item1.val = total

            if item1: item1 = item1.next
            if item2: item2 = item2.next

        return get_reversed(pointer)