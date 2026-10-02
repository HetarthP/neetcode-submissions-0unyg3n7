class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

      res=[] 

      n =len(nums)
      seen={} 

      for num in nums: 

        if num in seen: 
            seen[num]+=1 
        else:
            seen[num]=1 


      for key,val in seen.items(): 

        if val> n//3:
            res.append(key)

      return res 