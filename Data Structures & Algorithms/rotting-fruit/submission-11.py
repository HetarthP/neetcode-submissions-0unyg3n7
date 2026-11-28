class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n= len(grid) 
        q= deque() 

        fresh=0 

        minutes=0 

        dirs= [(1,0), (0,1), (-1,0), (0,-1)]

        rows,cols= len(grid), len(grid[0]) 

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==2:

                    q.append((r,c))
                else:

                    if grid[r][c]==1:
                        fresh+=1 
        

        while q and fresh>0: 

            for _ in range(len(q)): 

                r,c= q.popleft() 

                for dr,dc in dirs:

                    nr,nc = r+dr, c+dc 

                    if (nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]!=1):

                        continue 

                    grid[nr][nc]=2
                    q.append((nr, nc))
                    fresh-=1
            minutes+=1 
        if fresh==0:
            return minutes
        else:
            return -1 
            