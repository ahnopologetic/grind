# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy, while list1 or list2 append smallest to the dummy and move one fwd.

        # we need a tail to append!
        dummy = ListNode()
        tail = dummy
        
        if not list1 and not list2:
            return


        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if not list1:
            tail.next = list2
            tail = tail.next
        if not list2:
            tail.next = list1
            tail = tail.next
        
        return dummy.next

        
