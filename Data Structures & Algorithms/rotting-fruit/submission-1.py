from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 4 dirs

        #0= empty
        #1= fresh
        #2= rotten 

        #so rotten spread in 4 dirs every minute 

        minutes=0 

        n= len(grid) 

        rows,cols= len(grid), len(grid[0]) 

        q= deque()

        fresh=0 

        #initalize q 
        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1 

        dirs= [(1,0), (0,1), (-1,0),(0,-1)]

        while q and fresh>0:

            for _ in range(len(q)):

                r,c= q.popleft() 

                for dr,dc in dirs:

                    nr,nc= r+dr, c+dc 

                    if (nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]!=1):
                        continue 

                    grid[nr][nc]=2
                    q.append((nr,nc))
                    fresh-=1 
            minutes+=1 
        
        if fresh==0:
            return minutes
        return -1 


        