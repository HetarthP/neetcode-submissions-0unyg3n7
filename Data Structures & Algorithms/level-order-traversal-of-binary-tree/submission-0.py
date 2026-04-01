class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        queue = deque([root])
        res = []

        while queue:
            n = len(queue)
            level = []   # fresh list for this level

            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)  # append a *new* list every time

        return res
