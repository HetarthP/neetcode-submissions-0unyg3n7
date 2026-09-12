class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # -1= a water cell that cant be traversed 

        # 0= treasure chest 

        #2147483647= can be traversed 


        #fill each land cell with the distance to its nearest treasure 
        # so basically the big number --> 0 dist b/w them 

        #4 dirs 

        rows,cols= len(grid), len(grid[0])

        n= len(grid)

        q= deque() 

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==0:

                    q.append((r,c))


        dirs= [(1,0),(0,1), (-1,0), (0,-1)]

        while q: 

                r,c= q.popleft() 

                for dr,dc in dirs:

                    nr,nc= r+dr, c+dc

                    if (nr<0 or nr>=rows or nc<0 or nc>=cols):
                        continue 

                    if grid[nr][nc]!=2147483647:
                        continue 
                    grid[nr][nc]= grid[r][c]+1 

                    q.append((nr,nc))