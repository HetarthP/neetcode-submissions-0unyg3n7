class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stk=[] 

        for i in range(len(operations)):

            if operations[i] not in "+DC":
                stk.append(int(operations[i]))
            
            else:

                if operations[i]== "+":
                    stk.append(stk[-1] + stk[-2])
                
                elif operations[i]== "D":

                    stk.append(2* stk[-1])

                elif operations[i]=="C":
                    stk.pop()
        return sum(stk)