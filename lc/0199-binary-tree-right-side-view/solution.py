# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = {} # key: level, val: value
        level = 1

        q = deque([(root, level)])

        while q:
            node, nodelvl = q.popleft()

            result[nodelvl] = node.val

            if node.left:
                q.append((node.left, nodelvl+1))
            
            if node.right:
                q.append((node.right, nodelvl+1))
            
        
        return list(result.values())
