class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        res=[] 

        def bfs(root):

            if not root:
                return [] 

            q=deque([root]) 

            while len(q)>0:

                Rightside= None 

                for i in range(len(q)):

                    curr=q.popleft() 
                    Rightside = curr

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right) 
                if Rightside:
                    res.append(Rightside.val) 
            return res 
        return bfs(root)