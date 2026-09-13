class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        #connected horizontally or vertically 

        rows,cols= len(board), len(board[0]) 
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == 'O':
                    board[r][c] = 'S'
                    q.append((r,c))
        
        dirs= [(1,0),(0,1), (-1,0), (0,-1)]
        
        while q: 
            r,c= q.popleft()

            for dr,dc in dirs:
                nr,nc= r+dr, c+dc

                if nr<0 or nr>=rows or nc<0 or nc>=cols or board[nr][nc] != 'O':
                    continue 

                board[nr][nc] = "S"
                q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'