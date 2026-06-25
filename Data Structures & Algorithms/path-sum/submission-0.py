class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False 
        res=[]
        def dfs(root):
            if not root:
                return False

            res.append(root.val)
            
            if not root.left and not root.right:
                if sum(res) == targetSum:
                    return True
            
            if dfs(root.left) or dfs(root.right):
                return True
            
            res.pop()
            return False

        return dfs(root)