class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        #good subarray is where the nunber of diff ints = k 
        #sliding window with freq map 

        def atMost(k):

            l=0 
            count=0 
            seen={} 
            distinct=0 

            for r in range(len(nums)):

                if seen.get(nums[r],0)==0:
                    distinct+=1 
                seen[nums[r]]= seen.get(nums[r],0)+ 1

                while distinct>k:
                    seen[nums[l]]-=1 
                    if seen[nums[l]]==0:
                        distinct-=1 
                    l+=1 
                count+= r-l+1
            return count 
        return atMost(k)- atMost(k-1)
                 




                
        