class Solution:
    def isValid(self, s: str) -> bool:


        hm= {')':'(', '}':'{', ']':'['}
        stk=[]


        for bracket in s: 

            if bracket not in hm:
                stk.append(bracket)
            else:

                if not stk:
                    return False
                top= stk.pop() 
                if hm[bracket]!=top:
                    return False
            
        return not stk

        