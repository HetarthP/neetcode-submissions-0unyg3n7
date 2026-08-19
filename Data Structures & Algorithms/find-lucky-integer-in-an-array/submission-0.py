class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
       seen={}

       for num in arr:
        if num in seen:

            seen[num]+=1
        else:
            seen[num]=1

       res=[] 

       for key,val in seen.items():

            if val==key:
                res.append(key)
        
       return max(res) if res else -1