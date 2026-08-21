class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        seen= {} 

        for num in nums:

            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1

        res=[]
        for key,val in seen.items():
            
            if val >= 2:
                res.append(key)
        return max(res) if res else None