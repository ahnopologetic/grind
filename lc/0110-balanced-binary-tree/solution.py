# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height(root) >= 0
    
    def get_height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        lh, rh = self.get_height(root.left), self.get_height(root.right)
        # print("where are we?", root)
        if lh < 0 or rh < 0 or abs(lh - rh) > 1: return -1
        # print(lh, rh)
        return max(lh, rh) + 1
        
