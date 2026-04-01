class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stk=[]

        for p,s in sorted(zip(position,speed),reverse=True):

            if s==0:
                sec=float('inf')
            else:
                sec= (target - p) / s
            
            stk.append(sec)

            if len(stk)>=2 and stk[-1]<=stk[-2]:
                stk.pop()

        return len(stk)
        