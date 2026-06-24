class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        res=[]

        def dfs(root, depth):
            if not root:
                return
            res.append(depth)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        dfs(root, 1)
       
        return max(res)