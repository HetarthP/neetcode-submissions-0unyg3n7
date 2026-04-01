class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk=[]

        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stk.append(int(tokens[i]))
            else:
                a= stk.pop()
                b=stk.pop()

                if tokens[i]=="+":
                    res= stk.append(b+a)
                elif tokens[i]=="-":
                    res= stk.append(b-a)
                elif tokens[i]=="*":
                    res= stk.append(b*a)
                elif tokens[i]=="/":
                    res= stk.append(int(b/a))
            
        return stk[-1]


        