# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def dfs(node: Optional[TreeNode], depth:int, direction: str):
            self.longest = max(self.longest, depth)
            if node.left:
                dfs(node.left, depth+1, 'L') if direction != 'L' else dfs(node.left, 1, 'L')
            if node.right:
                dfs(node.right, depth+1, 'R') if direction != 'R' else dfs(node.right, 1, 'R')
                
        
        dfs(root, 0, '')
        return self.longest
