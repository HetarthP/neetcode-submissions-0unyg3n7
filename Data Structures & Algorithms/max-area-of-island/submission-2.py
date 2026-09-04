class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        #dfs because we're counting components
        #were gonna have land nodes connected by water edges 
        #easiest way will be to just run dfs and loop through
    
        if not grid:
            return 0 
        count=0 
        area=0
        max_area=0

        row,col= len(grid), len(grid[0])
        
        def dfs(r,c):

            if r<0 or r>= row or c<0 or c>=col or grid[r][c]!=1:
                return 0

            grid[r][c]=0

            return 1 + (\
            dfs(r+1,c) + \
            dfs(r-1,c) + \
            dfs(r,c+1) + \
            dfs(r,c-1))
            
            

        for r in range(row):
            for c in range(col):

                if grid[r][c]==1:
                    area= dfs(r,c) 
                    max_area= max(max_area,area)
        return max_area