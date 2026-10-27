# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        first_item = ListNode()
     
        first_item.next = head

        nums = set(nums)

        traversal_point = first_item

        while traversal_point and traversal_point.next:
            while traversal_point.next and traversal_point.next.val in nums:
                traversal_point.next = traversal_point.next.next
            
            
            traversal_point = traversal_point.next
        
        return first_item.next
