class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        #return number of subarrays of size k whose average is >= threshold 

        count=0
        summ=0

        l=0

        for r in range(len(arr)):

            summ+= arr[r]

            if r-l+1>k:

                summ-= arr[l]
                l+=1
            
            if r-l+1==k:
                if summ/k>=threshold:
                    count+=1
        return count 

            
        