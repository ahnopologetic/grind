# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        node = None
        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node


    
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = self.reverseLL(slow.next)
        first = head
        ans = 0

        while second_half:
            ans = max(ans, first.val + second_half.val)
            second_half = second_half.next
            first = first.next
    
        return ans
            
