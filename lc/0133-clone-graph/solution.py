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

        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, [])
        
        while q:
            n = q.popleft()

            for neigh in n.neighbors:
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val, [])
                    q.append(neigh)
                visited[n].neighbors.append(visited[neigh])

        return visited[node]

