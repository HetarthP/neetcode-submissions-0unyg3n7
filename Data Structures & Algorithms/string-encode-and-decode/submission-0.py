class Solution:

    def encode(self, strs: List[str]) -> str:
        emp=''

        for s in strs: 
            emp += str(len(s))+ "#"+ s

        return emp 

        
    def decode(self, s: str) -> List[str]:

        res=[]
        p1=0

        while p1<len(s):
            p2=p1
            while s[p2] != '#':
                p2+=1
            
            length= int(s[p1:p2])
            res.append(s[p2+1: p2+1+length])
            p1= p2+1+length
        return res

