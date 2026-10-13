class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        rows, cols = len(maze), len(maze[0])

        q = deque([start])
        visited = {tuple(start)}

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            r, c = q.popleft()

            if [r, c] == destination:
                return True

            for dr, dc in dirs:
                nr, nc = r, c

                while (0 <= nr + dr < rows and
                       0 <= nc + dc < cols and
                       maze[nr + dr][nc + dc] == 0):

                    nr += dr
                    nc += dc

                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))

        return False