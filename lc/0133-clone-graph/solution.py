"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        copy = Node(val=node.val)
        queue = deque([node])
        clone = {node.val: copy}

        while queue:
            curr = queue.popleft()
            curr_clone = clone[curr.val]

            for ngh in curr.neighbors:
                if ngh.val not in clone:
                    # clone[curr.val].neighbors.append(ngh)
                    clone[ngh.val] = Node(ngh.val)
                    queue.append(ngh)
                curr_clone.neighbors.append(clone[ngh.val])
        
        return clone[node.val]
            
        
        return result



        
