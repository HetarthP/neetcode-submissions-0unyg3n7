class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        if not arr:
            return 0 

        l=0 

        count=0 
        total=0 

        for r in range(len(arr)):

            total+= arr[r]

            if r-l+1>k:

                total-=arr[l]
                l+=1 
            
            if r-l+1==k:

                if total//k>= threshold:
                    count+=1
        return count 