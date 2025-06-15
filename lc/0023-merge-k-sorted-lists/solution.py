# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from collections import deque
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []

        for head in lists:
            # curr = head
            while head:
                heapq.heappush(result, head.val)
                head = head.next
        dummy = ListNode()
        curr = dummy
        while result:
            curr.next = ListNode(heapq.heappop(result))
            curr = curr.next
        
        return dummy.next
        
