class Solution:
    def isValid(self, s: str) -> bool:


        hm= {')':'(', '}':'{', ']':'['}
        stk=[]


        for bracket in s: 

            if bracket in hm:
                if not stk:
                    return False
                top= stk.pop() 
                if hm[bracket]!=top:
                    return False
            else:
                stk.append(bracket)
        
        if stk:
            return False
        else:
            return True

        