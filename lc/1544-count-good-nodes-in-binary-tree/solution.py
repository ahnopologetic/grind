# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # ans = 1, path = []
        # if max(path) == curr.val -> ans += 1
        # return ans

        # def dfs(node: Optional[TreeNode], maxval: int) -> int:

        #     if not node:
        #         return 0
            
        #     if node.val >= maxval:
        #         good = 1
        #     else:
        #         good = 0
            
        #     maxval = max(maxval, node.val)

        #     left = dfs(node.left, maxval)
        #     right = dfs(node.right, maxval)

        #     # print(f"{node.val=} {good=} {left=} {right=}")
        #     return good + left + right
        
        # return dfs(root, root.val)

        # bfs

        ans = 0
        q = deque([(root, root.val)])

        while q:
            node, maxval = q.popleft()

            if node.val >= maxval:
                ans += 1

            if node.left:
                q.append((node.left, max(maxval, node.val)))
            
            if node.right:
                q.append((node.right, max(maxval, node.val)))
        
        return ans
