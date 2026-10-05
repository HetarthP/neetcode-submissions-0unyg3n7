class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        stk=[] 

        for asteroid in asteroids: 

            while stk and asteroid<0 and stk[-1]>0: 
                diff= asteroid + stk[-1]

                if diff<0:
                    stk.pop() 
                elif diff>0:
                    asteroid=0 
                else:
                    asteroid=0 
                    stk.pop()
            if asteroid: 
                stk.append(asteroid)
        return stk  

            



