# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result

        def dfs(root: Optional[TreeNode], targetSum: int, path: list[int]):
            if not root:
                return 
            
            path.append(root.val)
            
            if not root.left and not root.right and targetSum == root.val:
                result.append(path[:])
            else:
                dfs(root.left, targetSum - root.val, path)
                dfs(root.right, targetSum - root.val, path)
            
            path.pop()

        dfs(root, targetSum, [])
        return result
        
