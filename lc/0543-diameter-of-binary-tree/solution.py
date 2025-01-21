# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.iterate_and_update(root)
        return self.diameter
    
    def iterate_and_update(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.iterate_and_update(root.left)
        right_depth = self.iterate_and_update(root.right)

        curr_diameter = left_depth + right_depth

        self.diameter = max(self.diameter, curr_diameter)
        return max(left_depth, right_depth) + 1

