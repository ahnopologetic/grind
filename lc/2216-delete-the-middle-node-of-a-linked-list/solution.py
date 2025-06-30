# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        prev = ListNode()
        prev.next = head
        slow = prev
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return prev.next
