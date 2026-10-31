class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l=0
        seen={} 

        distinct=0 
        res=0

        for r in range(len(fruits)):

            seen[fruits[r]]= seen.get(fruits[r],0)+1 

            if seen[fruits[r]]==1:
                distinct+=1 
            
            while distinct>2:

                seen[fruits[l]]-=1 

                if seen[fruits[l]]==0:
                    distinct-=1 
                l+=1 

            res= max(res, r-l+1)
        return res