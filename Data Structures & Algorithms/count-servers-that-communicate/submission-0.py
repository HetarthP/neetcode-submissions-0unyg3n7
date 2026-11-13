class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        rows,cols= len(grid), len(grid[0]) 
        rowCount, colCount= [0] * rows, [0] * cols

        count=0 

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==1:
                    rowCount[r]+=1 
                    colCount[c]+=1 
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    if rowCount[r]>1 or colCount[c]>1:
                        count+=1 
        return count 
