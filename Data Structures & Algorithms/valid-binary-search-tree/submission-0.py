# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:



        if not root:
            return False 

        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True  # empty subtree is valid

            # Current node must be strictly within (low, high)
            if not (low < node.val < high):
                return False

            # Left subtree: values < node.val; Right subtree: values > node.val
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))
        