class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #dfs because we're counting components
        #were gonna have land nodes connected by water edges 
        #easiest way will be to just run dfs and loop through
    
        if not grid:
            return 0 
        count=0 

        row,col= len(grid), len(grid[0])
        
        def dfs(r,c):

            if r<0 or r>= row or c<0 or c>=col or grid[r][c]!="1":

                return 
            
            grid[r][c]= "0"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(row):
            for c in range(col):

                if grid[r][c]=="1":
                    count+=1 
                    dfs(r,c)
        return count 



            