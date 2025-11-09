# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while q:
            node = q.popleft()
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)

            if not q:
                if temp:
                    levels.append([n.val for n in temp])
                q = temp
                temp = deque()
            
        return levels
