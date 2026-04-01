class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=0
        maxRight=0
        total_water=0
    
        l,r=0,len(height)-1
    
        while l<r:
            if height[l]<height[r]:
                maxLeft=max(maxLeft, height[l]) 
                
                total_water+=maxLeft-height[l]
                
                l+=1 
            else: 
                maxRight=max(maxRight,height[r]) 
                
                total_water+=maxRight-height[r]
                r-=1
            
        return total_water