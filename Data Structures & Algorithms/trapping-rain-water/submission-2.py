class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft=0 
        maxRight=0 

        l=0 

        r= len(height)-1
        totalWater=0


        while l<r: 

            if height[l]<height[r]:

                maxLeft= max(maxLeft, height[l])
                totalWater+= maxLeft - height[l]

                l+=1  

            else:

                 maxRight= max(maxRight, height[r])
                 totalWater+= maxRight - height[r]

                 r-=1 
        return totalWater


            