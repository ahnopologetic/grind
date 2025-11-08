# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # nodes = []
        # head = tail = ListNode(None)
        # for l in lists:
        #     while l:
        #         nodes.append(l.val)
        #         l= l.next
        
        # nodes = sorted(nodes)
        # for node in nodes:
        #     tail.next = ListNode(node)
        #     tail = tail.next
        
        # return head.next
        h = []
        head = tail = ListNode(0)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))

        while h:
            node = heapq.heappop(h)
            node = node[2]
            tail.next = node
            tail = tail.next
            if node.next:
                i+=1
                heapq.heappush(h, (node.next.val, i, node.next))

        return head.next
        

            

                

