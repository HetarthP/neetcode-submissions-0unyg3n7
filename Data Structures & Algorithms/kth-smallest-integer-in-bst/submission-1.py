class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res=[]

        def dfs(root):

            if not root:
                return 
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)

        res.sort()

        return res[k-1]