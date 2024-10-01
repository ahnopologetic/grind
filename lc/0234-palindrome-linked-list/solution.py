# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # reverse should be same
        vals = []
        rev_vals = []


        prev = None
        curr = head
        while curr is not None:
            next_ = curr.next
            vals.append(curr.val)
            curr.next = prev
            prev = curr
            curr = next_
        
        while prev:
            rev_vals.append(prev.val)
            prev = prev.next

        return vals == rev_vals
            
