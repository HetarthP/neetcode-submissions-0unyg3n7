class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        seen={}

        for c in s:

            if c in seen:
                seen[c]+=1
            else:
                seen[c]=1

        res=[]
        for key,val in seen.items():

            if val==1:
                res.append(key)

        if not res:
            return -1

        for i in range(len(s)):

            if s[i]==res[0]:
                return i
        return -1