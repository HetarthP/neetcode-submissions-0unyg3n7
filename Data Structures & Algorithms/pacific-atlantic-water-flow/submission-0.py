from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(q, visited):

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))


        pacific = set()
        atlantic = set()

        pacific_q = deque()
        atlantic_q = deque()


        # Pacific = top row
        for c in range(cols):
            pacific_q.append((0, c))
            pacific.add((0, c))

        # Pacific = left column
        for r in range(rows):
            pacific_q.append((r, 0))
            pacific.add((r, 0))


        # Atlantic = bottom row
        for c in range(cols):
            atlantic_q.append((rows - 1, c))
            atlantic.add((rows - 1, c))

        # Atlantic = right column
        for r in range(rows):
            atlantic_q.append((r, cols - 1))
            atlantic.add((r, cols - 1))


        bfs(pacific_q, pacific)
        bfs(atlantic_q, atlantic)


        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res