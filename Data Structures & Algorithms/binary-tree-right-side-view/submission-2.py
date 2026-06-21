class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[] 

        def bfs(root):
            if not root:
                return []
            q= deque([root])

            while len(q)>0:
                rightSide=None
                for i in range(len(q)):

                    curr=q.popleft()

                    if curr:
                        rightSide=curr 
                        if curr.left:
                            q.append(curr.left)
                        if curr.right:
                            q.append(curr.right)
                if rightSide:
                    res.append(rightSide.val)
            return res
        return bfs(root)