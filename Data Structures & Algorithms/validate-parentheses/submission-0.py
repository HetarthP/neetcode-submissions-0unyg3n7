class Solution:
    def isValid(self, s: str) -> bool:

        hm= { ')':'(','}':'{',']':'['}

        stk=[] 

        for c in s: 

            if c not in hm: #meaning open bracket
                stk.append(c)
            else:

                if not stk: #if stack is empty
                    return False 
                else: 
                    pop= stk.pop()
                    if pop!= hm[c]: #if the popped value isnt the same as hm value then return false 
                        return False 

        return not stk


        