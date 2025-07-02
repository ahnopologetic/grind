# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # maxlvl = 1
        # levelsum = [0]

        # q = deque([(root, 1)])

        # while q:
        #     node, lvl = q.popleft()
        #     if len(levelsum) < lvl:
        #         levelsum.append(0)

        #     levelsum[lvl-1] += node.val

        #     if node.left:
        #         q.append((node.left, lvl+1))
            
        #     if node.right:
        #         q.append((node.right, lvl+1))

        # # prefix sum


        # return maxlvl

        max_sum = root.val
        max_lvl = 1
        lvl = 1

        q = deque([root])

        while q:
            curr_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_lvl = lvl
            
            lvl += 1

        return max_lvl
                



