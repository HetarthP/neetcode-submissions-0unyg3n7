class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        seen={}
        res=[]

        for num in nums:

            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1

        
        for key,val in seen.items():

            if val> len(nums)//2:
                res.append(key)
        return max(res)