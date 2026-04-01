# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res=[]
        def right(node,depth):
            if not node:
                return 0 

            if depth==len(res):
                res.append(node.val)

            right(node.right,depth+1)
            right(node.left,depth+1)
        right(root,0)
        return res
        