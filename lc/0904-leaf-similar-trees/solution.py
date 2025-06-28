# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node: TreeNode) -> tuple:
            # stack = []
            # # how to iterate through trees?
            # while root:
            #     if root.left:
            #         root = root.left
            #         continue
            #     if root.right:
            #         root = root.right
            #         continue
            #     stack.append(root.val)
            # return tuple(stack)

            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            
            return get_leaves(node.left) + get_leaves(node.right)
                
                
        
        if not root1 or not root2:
            return False
        
        return get_leaves(root1) == get_leaves(root2)
