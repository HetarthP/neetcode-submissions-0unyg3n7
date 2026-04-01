class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        res=[0]*n
        stk=[]
        
        for i,j in enumerate(temperatures): 
            while stk and j>stk[-1][1]:
                stkInd,stkTemp= stk.pop()

                res[stkInd]= i- stkInd

            stk.append((i,j))
        return res



        