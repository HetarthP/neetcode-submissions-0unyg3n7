# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[] 

        def bfs(root):

            if not root:
                return []

            q =deque([root]) 

            while q: 
                
                level_vals=[]

                for i in range(len(q)):

                    curr=q.popleft() 

                    level_vals.append(curr.val)

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right) 
                res.append(level_vals)
            return res 
        return bfs(root) 