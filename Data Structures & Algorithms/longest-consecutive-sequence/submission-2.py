class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s=set()
        nums.sort()
        longest=0
        length=0
    
        for i in range(len(nums)): 
            if i>0 and nums[i]==nums[i-1]:
                
                continue
        
            if i>0 and nums[i]==nums[i-1]+1:
                length+=1
                
            else:
                length=1
            
            longest= max(longest, length)
    
            
            
            
        return longest
        

        