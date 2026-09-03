class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l=1 

        r= max(piles) 

        minspeed=r 

        while l<=r:

            mid= l+((r-l)//2)
            if mid == 0: mid = 1
            running = 0
            for i in range(len(piles)):

                running += math.ceil(piles[i]/mid) 

            if running>h:
                l=mid+1
            
            else:
                r=mid-1 

                minspeed= mid
        return minspeed