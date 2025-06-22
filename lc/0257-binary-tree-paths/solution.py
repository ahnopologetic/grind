# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def fn(root, s: str):
            if not root:
                return ""
            
            s += str(root.val)

            if not root.left and not root.right:
                result.append(s)
            
            fn(root.left, s + "->")
            fn(root.right, s + "->")
            
        fn(root, "")
        return result
        
