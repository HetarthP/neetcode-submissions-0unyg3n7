class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0 

        def dfs(i,j):

            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!=1:
                return 0 
            else:

                grid[i][j]=0
                return 1+dfs(i,j+1)+dfs(i,j-1)+dfs(i+1,j)+dfs(i-1,j)

        rows,cols= len(grid),len(grid[0])

        count= 0 

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==1:
                    count= max(count, dfs(r,c))
                
        return count
        