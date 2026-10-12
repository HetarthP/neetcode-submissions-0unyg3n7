class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        normal=[] 

        for num in heights:
            normal.append(num) 

        heights.sort() 

        count=0 

        #heights= expected 
        #normal = normal ordering 

        for i in range(len(normal)):
            if normal[i] != heights[i]:
                count+=1 
        return count